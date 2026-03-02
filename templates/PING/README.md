# Introduction

This template automatically send ICMP echo requests throughout many hosts around the world (customisable). The hosts to ping can easily be customized for any purposes.\
By default, the following hosts are queried:

* Asia (AS):
  * China: www.baidu.com
  * India: www.google.co.in
  * Japan: www.yahoo.co.jp
* Australia (AS): www.abc.net.au
* Central and Eastern Europe (CEE):
  * Poland: onet.pl
  * Russia: vk.com
* Middle East and North Africa (MENA):
  * Somalia: jazeerauniversity.edu.so
  * United Arab Emirates: uae-ed.metercdn.net
* North America (NA):
  * Canada: www.cbc.ca
  * United States: mit.edu
* Pacific Islands (PA):
  * New Zealand: www.nzherald.co.nz
* South America (SA):
  * Argentina: www.clarin.com
  * Brazil: uol.com.br
* Western Europe (WEU):
  * Germany: www.spiegel.de
  * Switzerland: cern.ch
* South Africa (ZA): www.naspers.com


## Installation

This template does not even require an agent: everything go through simple checks.

I recommend to add a dummy host called *Internet* and to simply link this template to it.


## Macros

The following host macros are configured:

|Name|Value|Description|
|----|-----|-----------|
|{$ICMP_LOSS_WARN}|20|Warning threshold of ICMP packet loss in %|
|{$ICMP_RESPONSE_TIME_WARN}|0.15|Warning threshold of the average ICMP response time in seconds|
|{$ICMP_TARGETS}|cern.ch,jazeerauniversity.edu.so,mit.edu,onet.pl,uae-ed.metercdn.net,uol.com.br,vk.com,www.abc.net.au,www.baidu.com,www.cbc.ca,www.clarin.com,www.google.co.in,www.naspers.com,www.nzherald.co.nz,www.spiegel.de,www.yahoo.co.jp|Comma-separated list of FQDNs/IPs to PING|

Although the macros *{$ICMP_LOSS_WARN}* and *{$ICMP_REPONSE_TIME_WARN}* exist, the relevant triggers that use these macros are created but **disabled** by default.


## Items

The following item is configured:

|Name|Type|Key|Formula|
|----|----|---|-------|
|Get data|Calculated|ping.targets.raw|"{$ICMP_TARGETS}"|

This item simply outputs the values defined in the host macro. All the relevant discovered objects are based on this item.


## Discovery Rules

The following discovery rule is configured:

|Name|Type|Key|Preprocessing|
|----|----|---|----------|
|Discover Ping Targets|Dependent item|ping.discovery|Name: Javascript, Value: `var targets = value.split(',');
var data = [];

for (var i = 0; i < targets.length; i++) {
    var t = targets[i].trim();
    if (t !== "") {
        data.push({ "{#ICMPTARGET}": t });
    }
}

return JSON.stringify({ data: data });`|

This preprocessing actually pushes a LLD macro called *{#ICMPTARGET}* which will be used by all prototypes items, triggers and graphs.


### Item Prototypes

One value mapping is configured in the template for the *Service state* of the ICMP echo request (up or down).\
The following item prototypes are configured:

|Name|Type|Key|
|----|----|---|
|{#ICMPTARGET} ICMP loss|Simple check|icmppingloss[{#ICMPTARGET}]|
|{#ICMPTARGET} ICMP ping|Simple check|icmpping[{#ICMPTARGET}]|
|{#ICMPTARGET} ICMP response time|Simple check|icmppingsec[{#ICMPTARGET}]|


### Trigger Prototypes

The following trigger prototypes are configured:

|Name|Expression|Severity|
|----|----------|--------|
|{#ICMPTARGET}: Unavailable by ICMP ping|max(/World Ping/icmpping[{#ICMPTARGET}],3)=0|High|
|{#ICMPTARGET}: High ICMP ping loss|(min(/World Ping/icmppingloss[{#ICMPTARGET}],5m)>{$ICMP_LOSS_WARN} and min(/World Ping/icmppingloss[{#ICMPTARGET}],5m)<100)|Warning|
|#{ICMPTARGET}: High ICMP ping response time|avg(/World Ping/icmppingsec[{#ICMPTARGET}],5m)>{$ICMP_RESPONSE_TIME_WARN}|Warning|


**NOTE**: all of those are created in a ***disabled*** state by default.


### Graph Prototypes

The following graph prototype is configured:

|Name|Graph Type|Items|
|----|----------|--------|
|{#ICMPTARGET} ICMP response time|Normal|Magvice - World Ping: {#ICMPTARGET} ICMP response time|


## Dashboards

One dashboard called *Internet Latency* simply outputs the ICMP response time graphs for every discovered target.
