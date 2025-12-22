# Introduction

This template is a mimic of *DownDetector*: it queries various Internet services and cloud providers for their status. It does not require any agents: only HTTP agent objects are configured (performed by either the *Zabbix* server or proxy).

## Usage
- Create a dummy host called *Internet* and assign it a SNMP interface (no need to configure it)
- Link the template to the dummy host

## Macros

N/A

## Template Links

N/A

## Discovery Rules

N/A

## Items

|Name|Description|Type|Key|
|----|-----------|----|----|
|Akamai Detailed Status|API call to the status page|HTTP agent|http_status_get_akamaidesc for detailed description|
|Akamai Status|API call to the status page|HTTP agent|http_status_get_akamai|
|Cloudflare Detailed Status|API call to the status page|HTTP agent|http_status_get_cloudflaredesc for detailed description|
|Cloudflare Status|API call to the status page|HTTP agent|http_status_get_cloudflare|
|Codabox Detailed Status|API call to the status page|HTTP agent|http_status_get_codaboxdesc for detailed description|
|Codabox Status|API call to the status page|HTTP agent|http_status_get_codabox|
|Github Detailed Status|API call to the status page|HTTP agent|http_status_get_githubdesc for detailed description|
|Github Status|API call to the status page|HTTP agent|http_status_get_github|
|Microsoft Azure Status|API call to the status page|HTTP agent|http_status_get_azure|
|Microsoft M365 Consumer Status|API call to the status page|HTTP agent|http_status_get_m365consumer|
|Microsoft Power Platform Status|API call to the status page|HTTP agent|http_status_get_ppac|
|Ookla Detailed Status|API call to the status page|HTTP agent|http_status_get_ookladesc for detailed description|
|Ookla Status|API call to the status page|HTTP agent|http_status_get_ookla|
|OVH Bare Metal Cloud Detailed Status|API call to the status page|HTTP agent|http_status_get_ovh_bmcdesc for detailed description|
|OVH Bare Metal Cloud Status|API call to the status page|HTTP agent|http_status_get_ovh_bmc|
|OVH Network Infrastructure Detailed Status|API call to the status page|HTTP agent|http_status_get_ovh_infradesc for detailed description|
|OVH Network Infrastructure Status|API call to the status page|HTTP agent|http_status_get_ovh_infra|

## Triggers

|Name|Description|Expression|Priority|
|----|-----------|----------|--------|
|AWS Status Page is DOWN|-|last(/Cloud Down Detector/web.test.fail[AWS])>0|Disaster|
|Google Cloud Status Page is DOWN|-|last(/Cloud Down Detector/web.test.fail[Google Cloud])>0|Disaster|
|Google Workspace Status Page is DOWN|-|last(/Cloud Down Detector/web.test.fail[Google Workspace])>0|Disaster|
|Major Incident at Provider: Akamai|-|last(/Cloud Down Detector/http_status_get_akamai)="major_outage"|Disaster|
|Major Incident at Provider: Cloudflare|-|last(/Cloud Down Detector/http_status_get_cloudflare)="major_outage"|Disaster|
|Major Incident at Provider: Codabox|-|last(/Cloud Down Detector/http_status_get_codabox)="major_outage"|High|
|Major Incident at Provider: Github|-|last(/Cloud Down Detector/http_status_get_github)="major_outage"|Average|
|Major Incident at Provider: Microsoft 365 (Consumers)|-|last(/Cloud Down Detector/http_status_get_m365consumer)="major_outage"|High|
|Major Incident at Provider: Microsoft Azure|-|last(/Cloud Down Detector/http_status_get_azure)="major_outage"|Disaster|
|Major Incident at Provider: Microsoft Power Platform|-|last(/Cloud Down Detector/http_status_get_ppac)="major_outage"|Warning|
|Major Incident at Provider: Ookla|-|last(/Cloud Down Detector/http_status_get_github)="major_ookla"|Warning|
|Major Incident at Provider: OVH|-|last(/Cloud Down Detector/http_status_get_ovh_bmc)="major_outage" or last(/Cloud Down Detector/http_status_get_ovh_infra)="major_outage"|High|

## Graphs

N/A

## Dashboards

One dashboard showing the status of all monitored services.

## Web Scenarios

One web scenario per service/provider is configured to provide additional statistics.
