from extras.plugins import PluginConfig

class NetboxDiscrepancy(PluginConfig):
    name = 'netbox_discrepancy'
    verbose_name = 'NetBox Discrepancy'
    description = 'A plugin to show discrepancies between NetBox and the real world'
    version = '0.1'
    base_url = 'discrepancy'

config = NetboxDiscrepancy