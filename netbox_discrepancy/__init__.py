from datetime import datetime, timezone
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

        from core.models import Job
        from .models import Discrepancy
        from .jobs import sync_discrepancies, ENQUEUED_STATUS

        if Job.objects.filter(
            name="Synchronize discrepancies",
            status__in=ENQUEUED_STATUS,
            scheduled__gt=datetime.now(timezone.utc),
        ).exists():
            return

        Job.enqueue(
            sync_discrepancies,
            instance=Discrepancy.objects.first(),
            name="Synchronize discrepancies",
            user=None,
            interval=5,
            schedule_at=datetime.now(timezone.utc),
        )


config = NetboxDiscrepancy
