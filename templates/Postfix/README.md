# Introduction
This template monitors a Postfix instance's processes and queues using the Zabbix Agent, pflogsumm, logtail, postqueue and a helper script.

Monitored items are:

* Number of different running Postfix processes
* CPU and Memory usage of different Postfix processes
* Postfix version
* Number of messages in different queue's
* Bounced, Deferred and Reject reasons
* Mail volumes delivered/received in bytes

## Requirements
  - Postfix
  - Zabbix Agent 2
  - Bash
  - Logtail
  - pflogsumm

## Setup

On the host with a running Postfix service you want to monitor:
  - Install the Zabbix Agent or Zabbix Agent 2 package if it is not yet installed on the host.
  - Install `logtail` and `pflogsumm`

```
apt install logtail pflogsumm
```

  - Create directory `/etc/zabbix/scripts`
  - Copy `files/scripts/postfix_get_spool.sh` to `/etc/zabbix/scripts` and ensure it is set executable.
  - Copy `files/sudoers.d/zabbix_postfix` to `/etc/sudoers.d`
  - Copy `files/zabbix_agentd.d/template_app_postfix.conf` to `/etc/zabbix/zabbix_agent2.d`

On Zabbix server:
  - Import the template into Zabbix
  - Assign the template to the host to monitor

### Macros used

|Name|Description|Default|
|----|-----------|-------|
|{$POSTFIX.ACTIVE.MAX} |<p>Max number of messages in Active queue</p>|`50` |
|{$POSTFIX.BOUNCE.MAX} |<p>Max number of bounced messages within POSTFIX.TRIGGER.PERIOD</p>|`50` |
|{$POSTFIX.DEFERRED.MAX} |<p>Max number of deferred messages in queue</p>| `50` |
|{$POSTFIX.HOLD.MAX} |<p>Max number of held messages in queue</p>|`200` |
|{$POSTFIX.REJECTED.MAX} |<p>Max number of rejected messages within POSTFIX.TRIGGER.PERIOD</p>|`20` |
|{$POSTFIX.TRIGGER.PERIOD} |<p>Time period to check for too many bounced or rejected mails. Context "bounced" or "rejected" is supported.</p>|`30m` |
|{$POSTFIX_USER} |<p>User running unprivileged postfix processes</p>|`postfix` |
