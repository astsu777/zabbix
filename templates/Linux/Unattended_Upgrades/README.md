# Introduction

This template monitors the *unattended-upgrades* package's activity.

## Installation

Please follow online instructions to configure *unattended-upgrades*: [Automatic updates](https://documentation.ubuntu.com/server/how-to/software/automatic-updates/).

## Macros

N/A

## Value Mappings

N/A

## Template Links

N/A

## Discovery Rules

N/A

## Items

The following item prototype is configured:

|Name|Description|Key
|----|-----------|---
|Auto-Fix DPKG|-|vfs.file.regmatch[/etc/apt/apt.conf.d/50unattended-upgrades,Unattended-Upgrade\:\:AutoFixInterruptedDpkg\s+\"true\"\;,UTF8,,]|
|Available Upgrades|-|system.run[/usr/bin/apt list --upgradable 2>/dev/null]|
|Check Unattended Upgrades|-|vfs.file.exists[/usr/bin/unattended-upgrade]|
|Debian Non-security Updates|-|vfs.file.regmatch[/etc/apt/apt.conf.d/50unattended-upgrades,^\s+\"o\=Debian\Wa\=stable\-updates\"\;,UTF8,,]|
|Debian Security Updates|-|vfs.file.regmatch[/etc/apt/apt.conf.d/50unattended-upgrades,^\s*\"origin\=Debian\Wcodename\=\$\{distro_codename}\Wlabel\=Debian\-Security\"\;,UTF8,,]|
|Log: Installed Upgrades|-|logrt[/var/log/unattended-upgrades/unattended-upgrades-dpkg.log,^Log\sstarted.*(\R.*?)+ended\:.(\d{4}-\d{2}-\d{2}\s+.\d{2}\:\d{2}:\d{2}),UTF8,20,,,]|
|Log: Unattended-Upgrades|-|logrt[/var/log/unattended-upgrades/unattended-upgrades.log,,UTF8,20,,,]|
|MOTD notifier|-|vfs.file.exists[/etc/update-motd.d/90-updates-available]|
|Reboot Required|-|vfs.file.exists[/var/run/reboot-required]|
|Remove-Unused-Kernel-Packages|-|vfs.file.regmatch[/etc/apt/apt.conf.d/50unattended-upgrades,Unattended-Upgrade\:\:Remove\-Unused\-Kernel\-Packages\s+\"true\"\;,UTF8,,]|
|Remove Unused Dependencies|-|vfs.file.regmatch[/etc/apt/apt.conf.d/50unattended-upgrades,Unattended-Upgrade\:\:Remove-Unused-Dependencies\s+\"true\"\;,UTF8,,]|
|Ubuntu Non-security Updates|-|vfs.file.regmatch[/etc/apt/apt.conf.d/50unattended-upgrades,\s+\"\$\{distro\_id}\:\$\{distro\_codename\}\-updates\"\;,UTF8,,]|
|Ubuntu Security Updates|-|vfs.file.regmatch[/etc/apt/apt.conf.d/50unattended-upgrades,^\s+\"\$\{distro\_id}\:\$\{distro\_codename\}\-security\"\;,UTF8,,]|
|Ubuntu Server Metapackage|-|system.run[/usr/bin/tasksel --list-tasks | /bin/grep 'Basic Ubuntu server']|

## Triggers

The following trigger prototype is configured:

|Name|Description|Expression|Priority|
|----|-----------|----------|--------|
|Auto-Fix DPKG is not enabled in /etc/apt/apt.conf.d/50unattended-upgrades|-|last(/Linux Unattended Upgrades/vfs.file.regmatch[/etc/apt/apt.conf.d/50unattended-upgrades,Unattended-Upgrade\:\:AutoFixInterruptedDpkg\s+\"true\"\;,UTF8,,])=0|Warning|
|Error {ITEM.LASTVALUE} when installing unattended-upgrades|-|find(/Linux Unattended Upgrades/logrt[/var/log/unattended-upgrades/unattended-upgrades.log,,UTF8,20,,,],,"like","ERROR")=1|Average|
|Remove-Unused-Dependencies is not enabled in /etc/apt/apt.conf.d/50unattended-upgrades|-|last(/Linux Unattended Upgrades/vfs.file.regmatch[/etc/apt/apt.conf.d/50unattended-upgrades,Unattended-Upgrade\:\:Remove-Unused-Dependencies\s+\"true\"\;,UTF8,,])=0|Warning|
|The host needs to be restarted|-|avg(/Linux Unattended Upgrades/vfs.file.exists[/var/run/reboot-required],24h)=1|Information|
|Unattended-upgrades package is not installed|-|last(/Linux Unattended Upgrades/vfs.file.exists[/usr/bin/unattended-upgrade])=0|Warning|
|Updates are available|-|find(/Linux Unattended Upgrades/system.run[/usr/bin/apt list --upgradable 2>/dev/null],,"like","upgradable from")=1|Information|
|Updates have been installed|-|nodata(/Linux Unattended Upgrades/logrt[/var/log/unattended-upgrades/unattended-upgrades-dpkg.log],4h)=0|Information|

## Graphs

N/A

## Dashboards

N/A
