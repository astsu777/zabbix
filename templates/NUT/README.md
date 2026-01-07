# Introduction

This template retrieves information about any UPS from a *NUT* server.

## Installation

*NUT* must be installed on a machine that can access the UPS information.

## Macros

The following macros are configured:

|Name|Value|Description|
|----|-----|-----------|
|{$NUT_SERVER}|-|FQDN/IP address of the remote NUT server|
|{$UPS_NAME}|ups|Name of the remote UPS|

## Template Links

N/A

## Discovery Rules

N/A

## Items

The following items are configured:

|Name|Type|Key|
|----|----|---|
|UPS Battery Charge|Zabbix agent|system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null battery.charge]|
|UPS Battery Runtime|Zabbix agent|system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null battery.runtime]|
|UPS Battery Status|Zabbix agent|system.run[status=$(upsc {$UPS_NAME}@{$NUT_SERVER} battery.charger.status 2>/dev/null) && case "$status" in "charging") echo 1 ;; "discharging") echo 2 ;; "floating") echo 3 ;; "resting") echo 4 ;; \*) echo 0 ;; esac]|
|UPS Device Model|Zabbix agent|system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null device.model]|
|UPS Load|Zabbix agent|system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null ups.power]|
|UPS Manufacturer|Zabbix agent|system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null device.mfr]|
|UPS Self Test|Zabbix agent|system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null ups.test.result]|
|UPS Status|Zabbix agent|system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null ups.status | grep -q 'OL' && echo '0' || echo '1']|
|UPS Total Power|Zabbix agent|system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null ups.power.nominal]|

Two value mappings are configured in the template for the *UPS Battery Status* and the *UPS Status*.


## Triggers

The following items are configured:

|Name|Expression|Severity|
|----|----------|--------|
|Battery capacity is critical|last(/NUT/system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null battery.charge],#1)<20|High|
|Battery capacity is low|last(/NUT/system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null battery.charge],#1)<50|Average|
|UPS is not detected|bitlength(last(/NUT/system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null device.model]))=0|High|
|UPS is running on battery|last(/NUT/system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null ups.status | grep -q 'OL' && echo '0' || echo '1'])<>0|Disaster|
|UPS self test failed|find(/NUT/system.run[/usr/bin/upsc {$UPS_NAME}@{$NUT_SERVER} 2>/dev/null ups.test.result],,"like","Done and passed")=0|High|


## Graphs

The following graphs are configured:

* UPS Battery: represents the battery charge and its current lifetime
* UPS Power: represents the current load compared to the total power output


## Dashboards

One dashboard containing all the above information is embedded in the template.
