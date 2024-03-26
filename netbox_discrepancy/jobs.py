from datetime import datetime, timedelta, timezone
from core.models import Job
import logging
from core.choices import JobStatusChoices
from time import sleep

logger = logging.getLogger(__name__)

ENQUEUED_STATUS = [
    JobStatusChoices.STATUS_PENDING,
    JobStatusChoices.STATUS_RUNNING,
    JobStatusChoices.STATUS_SCHEDULED,
]

# https://github.com/netbox-community/netbox/blob/d2fee886001e4abbcb1b4d9ed3fd32521c820be9/netbox/extras/reports.py#L30


def sync_discrepancies(job: Job, *args, **kwargs):
    """
    Synchronize discrepancies between NetBox and the real world, scheduled to run every 1 minute
    """

    try:
        job.start()
        print("WE ARE SYNCHRONIZING DISCREPANCIES 01")
        sleep(60)
        job.terminate()

    except Exception as e:
        job.terminate(status=JobStatusChoices.STATUS_ERRORED, error=repr(e))

    finally:
        if job.interval and not Job.objects.filter(
            name="Synchronize discrepancies",
            status__in=ENQUEUED_STATUS,
            scheduled__gt=datetime.now(
                timezone.utc)).exists():
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
