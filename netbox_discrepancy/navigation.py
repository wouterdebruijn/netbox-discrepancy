from extras.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_discrepancy:overview",
        link_text="Overview",
        permissions=["netbox_discrepancy.overview"]
    ),
    PluginMenuItem(
        link="plugins:netbox_discrepancy:discrepancy_list",
        link_text="Discrepancies",
        permissions=["netbox_discrepancy.view_discrepancy"]
    ),
    PluginMenuItem(
        link="plugins:netbox_discrepancy:discrepancytype_list",
        link_text="Discrepancy Types",
        permissions=["netbox_discrepancy.view_discrepancytype"]
    ),
)
