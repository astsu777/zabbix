# Introduction
This repository contains cloned versions of the built-in Zabbix templates. Some of them were modified and all modifications are documented here.

If some of them are not modified  at all, it is still best practice to use cloned templates in order to avoid breaking things when upgrading template versions.

All templates were cloned from **v7.4-1**.


# Template: Linux by Zabbix agent

The modifications in this template are related to decrease the severity of two triggers to avoid unnecessary trigger actions based on severity.

### Triggers

The following triggers have been modified::

|Name|Description|Key|Severity|
|----|-----------|---|--------|
|Linux: Number of installed packages has been changed|-|-|From WARNING to INFO|
|Linux: {HOST.NAME} has been restarted|-|-|From WARNING to INFO|


# Template: Proxmox VE by HTTP

The modifications in this template have been in order to avoid *Zabbix* discovery of some virtual machines and containers. Indeed, when deploying some VMs/LXCs for test purposes, it is preferrable to not have them being monitored.

### Template Macros

The following macros have been added at the template level:

|Name|Description|Value|
|----|-----------|-----|
|{$LXC.NAME.NOT_MATCHES}|Do not discover LXCs with the following names|^(?:LAB.\*\|lab.\*\|template.\*\|TEMPLATE.\*)$|
|{$QEMU.NAME.NOT_MATCHES}|Do not discover VMs with the following names|^(?:LAB.\*\|lab.\*\|template.\*\|TEMPLATE.\*)$|

### Discovery Rules

In order to use the above macros, the following discovery rules have been modified:

|Name|Label Macro|Operator|Regular Expression|
|----|-----------|--------|------------------|
|LXC discovery|{#LXC.NAME}|does not match|{$LXC.NAME.NOT_MATCHES}|
|QEMU discovery|{#QEMU.NAME}|does not match|{$QEMU.NAME.NOT_MATCHES}|


# Resources

Here are some useful resources you might want to check:

- [Zabbix Update All Templates](https://github.com/Udeus/Zabbix-Update-All-Templates): this repository by *Udeus* hosts a project that allows updating all templates at once
