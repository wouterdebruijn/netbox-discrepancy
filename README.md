# Netbox Discrepancy Plugin

This plugin is designed to compare the data in Netbox with the data in the real
world. It will compare the data in Netbox with the data in the real world and
report any discrepancies.

## Features

- 🗃️ Report discrepancies for Netbox devices
- 🔄 Compare real world data to Netbox

## Installation

```bash
# Don't install this yet, it's not ready
```

## Development Information

```bash
# Add the netbox directory to the python path
echo ~/Documents/Netbox/netbox/netbox > venv/lib/python3.12/site-packages/netbox.pth
```

```bash
# Run tests for this plugin
python3 netbox/netbox/manage.py test netbox_discrepancy.tests --keepdb --parallel 4
```
