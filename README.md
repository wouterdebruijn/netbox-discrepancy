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

As part of the plugin repository, the development folder contains a full netbox
development environment. This environment is partly dockerized for ease of use.

```bash
# Change directory to the development folder
cd development

# Start required services
docker-compose up -d

# Make any required changes in the configuration.py file. This will be copied to the netbox configuration folder on setup.

# Run initial setup
bash setup.sh
```
