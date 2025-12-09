# Introduction

This template retrieves statistics from *Caddy* using its embedded metrics server. It uses a *HTTP agent* key, meaning the *Zabbix* server (or proxy) will attempt to connect to the *Caddy* web server remotely.

## Installation

- Enable the *metrics* server in *Caddy* and replace the *<ZABBIX_IP>* with either the *Zabbix* server/proxy IP address:

```
{
  servers {
    metrics
  }
}

:48080 {
  @blocked not remote_ip <ZABBIX_IP>
  respond @blocked 444
  metrics /metrics
}
```

**NOTE**: the IP control on the server is not mandatory but it is recommended to only allow the monitoring server to access this virtual host.

## Macros

The following macros are configured:

|Name|Value|Description|
|----|-----|-----------|
|{$CADDY.HOST}|127.0.0.1|Caddy host IP|
|{$CADDY.PATH}|/metrics|Metrics path|
|{$CADDY.PORT}|48080|Metrics port|

## Template Links

N/A

## Discovery Rules

The following discovery rules are configured:

|Name|Key|Description|
|----|---|-----------|
|caddy_admin_http_requests_total|caddy_admin_http_requests_total|Number of admin HTTP requests|
|caddy_admin_http_requests_errors_total|caddy_admin_http_requests_errors_total|Number of admin HTTP requests in error|
|caddy_http_requests_in_flight|caddy_http_requests_in_flight|Number of HTTP requests in flight|
|caddy_http_requests_total|caddy_http_requests_total|Number of HTTP requests|
|caddy_http_request_duration_seconds_bucket|caddy_http_request_duration_seconds_bucket|Duration of HTTP requests (bucket)|
|caddy_http_request_duration_seconds_count|caddy_http_request_duration_seconds_count|Duration of HTTP requests (count)|
|caddy_http_request_duration_seconds_sum|caddy_http_request_duration_seconds_sum|Duration of HTTP requests (sum)|
|caddy_http_request_size_bytes_bucket|caddy_http_request_size_bytes_bucket|Size of HTTP requests (bucket)|
|caddy_http_request_size_bytes_sum|caddy_http_request_size_bytes_sum|Size of HTTP requests (sum)|
|caddy_http_response_duration_seconds_bucket|caddy_http_response_duration_seconds_bucket|Duration of HTTP responses (bucket)|
|caddy_http_response_duration_seconds_sum|caddy_http_response_duration_seconds_sum|Duration of HTTP responses (sum)|
|caddy_http_response_size_bytes_bucket|caddy_http_response_size_bytes_bucket|Size of HTTP reponses (bucket)|
|caddy_http_response_size_bytes_sum|caddy_http_response_size_bytes_sum|Size of HTTP reponses (sum)|
|caddy_reverse_proxy_upstreams_healthy|caddy_reverse_proxy_upstreams_healthy|Health of upstream proxied servers|


One item prototype is configured per discovery rule.

## Items

All statistics provided by *Caddy* metrics are collected.

## Triggers

N/A

## Graphs

N/A

## Dashboards

N/A
