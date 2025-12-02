# Zabbix Export Configuration
This script performs the following:

- Export all Zabbix configuration to a JSON file. This includes:
  * Hosts
  * Host groups
  * Maps
  * Images
  * Templates
  * Template groups

- Push the backup to a *Git* repository for versioning and diffs

# Configuration
It is necessary to provide the URL to the *Zabbix* API and also the API token for authentication.
