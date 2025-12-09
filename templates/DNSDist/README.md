# Introduction

This template retrieves statistics from *DNSDist* using its embedded Web server. It uses a *HTTP agent* key, meaning the *Zabbix* server (or proxy) will attempt to connect to the *DNSDist* web server remotely.

## Installation

- Generate a password hash:

```
$ sudo dnsdist -c
> hashPassword('changeme')
$scrypt$ln=10,p=1,r=8$kEEUvPsb05DU8C5U7/1TpA==$nyolI7rQRNaJVYF9ty8qw3I3XbIvcqoeUvoKcvousdk=
```

- Enable the [dnsdist webserver](https://dnsdist.org/guides/webserver.html):

```
webserver('127.0.0.1:8083')
setWebserverConfig({password="hash_from_above", apiKey="hash_from_above", acl="<ZABBIX_SERVER_IP>"})
```

## Macros

The following macros are configured:

|Name|Value|Description|
|----|-----|-----------|
|{$DNSDIST.APIKEY}|changeme|API key generated for DNSDist Web server|
|{$DNSDIST.WEBSERVER.IP}|127.0.0.1|DNSDist Web server IP address|
|{$DNSDIST.WEBSERVER.PORT}|8083|DNSDist Web server port|

## Template Links

N/A

## Discovery Rules

N/A

## Items

All statistics provided by *DNSdist* are collected.

## Triggers

The following triggers are configured:

|Name|Description|Expression|Priority|
|----|-----------|----------|--------|
|dnsdist security status unknown|The system cannot check for security vulnerabilities in the system's repository|last(/DNSDist/dnsdist.security-status)=0|Information|
|dnsdist service is not running|*DNSDist* service is not running|last(/DNSDist/proc.num[dnsdist])=0|High|
|dnsdist upgrade is recommended|*DNSDist* should be updated|last(/DNSDist/dnsdist.security-status)=2|Warning|
|dnsdist upgrade is mandatory|*DNSDist* needs to be updated due to a known vulnerability|last(/DNSDist/dnsdist.security-status)=3|Warning|

## Graphs

The following graphs are configured:

|Name|Description|
|----|-----------|
|dnsdist - Cache|Returns values for hits and misses in the cache|
|dnsdist - Latency|Average latency over time|
|dnsdist - Queries & Answers|Returns queries per seconds and the status of answers|
|dnsdist - Rules|Returns what rules matched DNS requests|

## Dashboards

N/A
