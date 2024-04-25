from datetime import datetime, timezone
import sys
from extras.plugins import PluginConfig

# Job Enqueue
# https://github.com/netbox-community/netbox/blob/d2fee886001e4abbcb1b4d9ed3fd32521c820be9/netbox/core/models/data.py#L156


class NetboxDiscrepancy(PluginConfig):
    name = 'netbox_discrepancy'
    verbose_name = 'NetBox Discrepancy'
    description = 'A plugin to show discrepancies between NetBox and the real world'
    version = '0.1'
    base_url = 'discrepancy'

    def ready(self):
        super().ready()

        # Check if we are starting django
        if 'runserver' not in sys.argv:
            return

        from core.models import Job
        from .jobs import sync_discrepancies, ENQUEUED_STATUS
        from dcim.models import Device

        query = Job.objects.filter(
            name="Synchronize discrepancies",
            status__in=ENQUEUED_STATUS,
        )

        # Delete and unschedule any existing jobs
        if query.exists():
            for job in query:
                job.delete()

        print("Enqueuing job")

        if Device.objects.count() == 0:
            print("No devices to sync")
            return

        Job.enqueue(
            sync_discrepancies,
            instance=Device.objects.first(),
            name="Synchronize discrepancies",
            user=None,
            interval=60,
            schedule_at=datetime.now(timezone.utc),
        )


config = NetboxDiscrepancy
