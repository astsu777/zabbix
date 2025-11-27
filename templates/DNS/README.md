# DNS
This template creates three host macros that need to be customized:

- **{$DNS_RECORD}**: value for of the DNS record to check (eg.: google.com)
- **{$DNS_RECORD_TYPE}**: type of DNS record (A, PTR, MX, etc...)
- **{$DNS_SERVER_IP}**: IP address/FQDN of the DNS server to query

# External DNS
This template creates two host macros may be customized:

- **{$EXT_DNS_RECORD}**: value for of the DNS record to check (eg.: amazon.com)
- **{$EXT_DNS_RECORD_TYPE}**: type of DNS record (A, PTR, MX, etc...)

