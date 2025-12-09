# Introduction

This template and its script allows monitoring the status of VRRP instances configured in *Keepalived*.

The VRRP instance notifies the script when a change happens and write the status to a file. The *Zabbix* agent then reads the content of the file with *vfs.file.regmatch* and reports it to the *Zabbix* server.

## Usage
- Copy the script to the *keepalived* node into */usr/local/bin/keepalived_notify.sh*
- Make it executable and owned by root:

```
chmod 751 /usr/local/bin/keepalived_notify.sh
chown root:root /usr/local/bin/keepalived_notify.sh
```

- Add the *notify* parameter to the *Keepalived* config:

```
vrrp_instance VRRP_1 {
    [...]
    notify "/usr/local/bin/keepalived_notify.sh"
}
```

## Macros

N/A

## Template Links

N/A

## Discovery Rules

N/A

## Items

|Name|Description|Type|Key and additional info|
|----|-----------|----|----|
|Keepalived: is BACKUP|<p>-</p>|`Zabbix agent`|vfs.file.regmatch[/var/run/keepalived_status,^.*(BACKUP)]<p>Update: 2m</p>|
|Keepalived: is MASTER|<p>-</p>|`Zabbix agent`|vfs.file.regmatch[/var/run/keepalived_status,^.*(MASTER)]<p>Update: 2m</p>|
|Keepalived: process count|<p>-</p>|`Zabbix agent`|proc.num[keepalived]]<p>Update: 2m</p>|

## Triggers

|Name|Description|Expression|Priority|
|----|-----------|----------|--------|
|Keepalived: state change from BACKUP to MASTER|<p>-</p>|<p>**Expression**: {Template App Keepalived:vfs.file.regmatch[/var/run/keepalived_status,^.*(MASTER)].prev()}=0 and {Template App Keepalived:vfs.file.regmatch[/var/run/keepalived_status,^.*(MASTER)].last()}=1</p><p>**Recovery expression**: </p>|average|
|Keepalived: state change from MASTER to BACKUP|<p>-</p>|<p>**Expression**: {Template App Keepalived:vfs.file.regmatch[/var/run/keepalived_status,^.*(MASTER)].prev()}=1 and {Template App Keepalived:vfs.file.regmatch[/var/run/keepalived_status,^.*(MASTER)].last()}=0</p><p>**Recovery expression**: </p>|average|
|Keepalived: state is BACKUP but it's stopped|<p>-</p>|<p>**Expression**: {Template App Keepalived:vfs.file.regmatch[/var/run/keepalived_status,^.*(MASTER)].last()}=0 and {Template App Keepalived:proc.num[keepalived].last()}<2</p><p>**Recovery expression**: </p>|high|
|Keepalived: state is MASTER but it's stopped|<p>-</p>|<p>**Expression**: {Template App Keepalived:vfs.file.regmatch[/var/run/keepalived_status,^.*(MASTER)].last()}=1 and {Template App Keepalived:proc.num[keepalived].last()}<2</p><p>**Recovery expression**: </p>|disaster|

## Graphs

N/A

## Dashboards

N/A
