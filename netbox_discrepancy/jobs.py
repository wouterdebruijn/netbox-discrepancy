from requests import Session
from datetime import datetime, timedelta, timezone
from core.models import Job
import logging
from core.choices import JobStatusChoices
from urllib.parse import urljoin
from dcim.models import Device, Interface
from netbox_discrepancy.models import Discrepancy, DiscrepancyType
from django_rq import job

logger = logging.getLogger(__name__)

ENQUEUED_STATUS = [
    JobStatusChoices.STATUS_PENDING,
    JobStatusChoices.STATUS_RUNNING,
    JobStatusChoices.STATUS_SCHEDULED,
]

# https://github.com/netbox-community/netbox/blob/d2fee886001e4abbcb1b4d9ed3fd32521c820be9/netbox/extras/reports.py#L30


class NetgazerSession(Session):
    def request(self, method, url, *args, **kwargs):
        url = urljoin("http://nc-hlm-dev001.intra.netco.nl:8080/", url)
        return super().request(method, url, *args, **kwargs)


connection = NetgazerSession()
connection.auth = ("admin", "admin")


@job('default', timeout='1h')
def sync_discrepancies(job: Job, *args, **kwargs):
    """
    Synchronize discrepancies between NetBox and the real world, scheduled to run every 1 minute
    """

    try:

        job.start()

        nb_devices = Device.objects.all()

        ng_devices = connection.get(
            "devices").json()

        for nb_device in nb_devices:
            for ng_device in ng_devices:
                if nb_device.name == ng_device["name"]:
                    logger.info(
                        f"Device {nb_device.name} found in NetBox and NetBox")

                    details = connection.get(
                        f"devices/{ng_device['id']}/").json()

                    interfaces = details['interfaces']

                    for interface in interfaces:
                        if not Interface.objects.filter(
                            device=nb_device,
                            name=interface['name']
                        ).exists():
                            [item, created] = DiscrepancyType.objects.get_or_create(
                                name="Interface not found in NetBox"
                            )

                            Discrepancy.objects.get_or_create(
                                device=nb_device,
                                type=item,
                                message=f"Interface {
                                    interface['name']} not found in NetBox"
                            )

                            continue

                        if interface['ipv4'] == None:
                            continue

                        if not Interface.objects.filter(
                            device=nb_device,
                            name=interface['name'],
                            ip_addresses__address=f'{
                                interface['ipv4']}/{interface["ipv4_mask"]}'
                        ).exists():

                            [item, created] = DiscrepancyType.objects.get_or_create(
                                name=f"IP address not found in NetBox"
                            )

                            Discrepancy.objects.get_or_create(
                                device=nb_device,
                                type=item,
                                message=f"IP address {
                                    interface['ipv4']}/{interface['ipv4_mask']} not found on {interface['name']} in NetBox"
                            )

                    nb_device.comments = details
                    nb_device.save()

                else:
                    logger.info(
                        f"Device {nb_device.name} not found in NetBox and NetBox")

        job.terminate()

    except Exception as e:
        logger.error(f"An error occurred: {repr(e)}")
        job.terminate(status=JobStatusChoices.STATUS_ERRORED, error=repr(e))

    finally:
        if job.interval and not Job.objects.filter(
            name="Synchronize discrepancies",
            status__in=ENQUEUED_STATUS,
            scheduled__gt=datetime.now(timezone.utc)
        ).exists():
            new_scheduled_time = job.scheduled + \
                timedelta(minutes=job.interval)
            job.enqueue(
                sync_discrepancies,
                instance=job.object,
                name=job.name,
                user=job.user,
                schedule_at=new_scheduled_time,
                interval=job.interval,
            )
