# Introduction

This template retrieves information about any Backblaze B2 buckets so they can be monitored.


## Installation

This template relies on an external script and also on the backblaze B2 CLI tool to be installed.
Follow these steps to properly use this template:

* Install the *Backblaze B2 CLI Tool* (on *Debian*, the binary name is *backblaze-b2*)
* Store the *backblaze_b2_lld.sh* script into directory */usr/lib/zabbix/externalscripts*
* Make sure the script is executable by *Zabbix*:

```bash
chown zabbix:zabbix backblaze_b2_lld.sh
chmod u+x backblaze_b2_lld.sh
```

* On the *Backblaze* Web portal, create an *applicationID* that will be used by *Zabbix*. This script should have R/O
  permissions against all buckets to be monitored
* Run the command *sudo -u zabbix backblaze-b2 account authorize* and provide the necessary information


**NOTE**: if the binary **is not** *backblaze-b2*, please modify the script to the correct name


## Backblaze Pricing

*Backblaze* offers a certain amount of transactions for free by default. These transactions also include API calls: some are free and others are free up until a certain threshold is reached. **It is strongely advised** to **configure caps/alerts** on your *Backblaze* account to make sure your budget does not go overboard. All the necessary information about this is available on this page: [Understand Backblaze B2 Data Caps and Alerts](https://www.backblaze.com/docs/cloud-storage-data-caps-and-alerts).


## Macros

The following host macros are configured:

|Name|Value|Description|
|----|-----|-----------|
|{$B2.PUSED.CRIT}|90|The critical threshold of the bucket utilization|
|{$B2.PUSED.WARN}|80|The warning threshold of the bucket utilization|
|{$B2_MAX_GROWTH_1H:"BUCKETNAME"}|<SIZE_IN_BYTES>|Threshold for size growth per hour (optional)|
|{$B2_MAX_SIZE:"BUCKETNAME"}|<SIZE_IN_BYTES>|Threshold for maximum size of the bucket (optional)|

The macros *{$B2_MAX_GROWTH_1H:"BUCKETNAME"}* and *{$B2_MAX_SIZE:"BUCKETNAME"}* need to be manually cloned and defined **only if you wish to get alerts on certain buckets**. In order to properly control the budget for a bucket, you can define its maximum theoritical size and also how much it grows on average per hour (sizes are in bytes).

For example, if a bucket name is **MYBUCKET** and it should not grow over 50GB per hour and its maximum size should not tip over 5TB, then define the macros like this on the host:

* {$B2_MAX_GROWTH_1H:"MYBUCKET"} with a value of 53687091200 (1 GiB = 1024^3 * 50)
* {$B2_MAX_SIZE:"MYBUCKET"} with a value of 5497558138880 (1 TiB = 1024^4 * 5)

To calculate the size in bytes, refer to the binary value:

* 1 KiB = 1024 bytes
* 1 MiB = 1024 KiB (so, 1024^2)
* 1 GiB = 1024 MiB (so, 1024^3)
* 1 TiB = 1024 GiB (so, 1024^4)


## Items

The following items are configured:

|Name|Type|Key|
|----|----|---|
|B2 Bucket Information|External check|backblaze_b2_lld.sh[discover]|

This is the master item that will perform API calls towards Backblaze. The item prototypes per bucket are dependent items so they do not trigger additional API calls towards Backblaze (with some exceptions).


## Discovery Rules

The following discovery rules are configured:

|Name|Type|Key|LLD Macros|
|----|----|---|----------|
|Buckets Discovery|Dependent item|b2.discovery|{#BUCKETNAME}|


### Item Prototypes

Three value mappings are configured in the template for the *Bucket Type*, *File Lock* and *SSE*.

|Name|Type|Key|
|----|----|---|
|B2 [{#BUCKETNAME}] File Count|External check|backblaze_b2_lld.sh[filecount,{#BUCKETNAME}]|
|B2 [{#BUCKETNAME}] File Lock|Dependent item|b2.bucket.filelock[{#BUCKETNAME}]|
|B2 [{#BUCKETNAME}] ID|Dependent item|b2.bucket.id[{#BUCKETNAME}]|
|B2 [{#BUCKETNAME}] Size|External check|backblaze_b2_lld.sh[size,{#BUCKETNAME}]|
|B2 [{#BUCKETNAME}] SSE|Dependent item|b2.bucket.sse[{#BUCKETNAME}]|
|B2 [{#BUCKETNAME}] Type|Dependent item|b2.bucket.type[{#BUCKETNAME}]|

The items for the file count and the size trigger API calls towards Backblaze. In total, 3 API calls are mare every 15 minutes to Backblaze B2 (1 global + 2 per bucket). All those calls are classified as *Transactions Class C* (see pricing at [Backblaze B2 Cloud Storage API Pricing Explained](https://www.backblaze.com/cloud-storage/transaction-pricing)).


### Trigger Prototypes

The following items are configured:

|Name|Expression|Severity|
|----|----------|--------|
|B2: Bucket [{#BUCKETNAME}]: File lock status has changed|change(/Backblaze B2/b2.bucket.filelock[{#BUCKETNAME}])<>0|Warning|
|B2: Bucket [{#BUCKETNAME}]: ID has changed|change(/Backblaze B2/b2.bucket.id[{#BUCKETNAME}])<>0|Average|
|B2: Bucket [{#BUCKETNAME}]: Rapid growth in the last hour|last(/Backblaze B2/backblaze_b2_lld.sh[size,{#BUCKETNAME}]) - avg(/Backblaze B2/backblaze_b2_lld.sh[size,{#BUCKETNAME}],1h) > {$B2_MAX_GROWTH_1H:"{#BUCKETNAME}"}|Information|
|B2: Bucket [{#BUCKETNAME}]: Running out of free disk space|last(/Backblaze B2/backblaze_b2_lld.sh[size,{#BUCKETNAME}])>{$B2_MAX_SIZE:"{#BUCKETNAME}"} * {$B2.PUSED.WARN} / 100|Warning|
|B2: Bucket [{#BUCKETNAME}]: Running out of free disk space|last(/Backblaze B2/backblaze_b2_lld.sh[size,{#BUCKETNAME}])>{$B2_MAX_SIZE:"{#BUCKETNAME}"} * {$B2.PUSED.CRIT} / 100|Average|
|B2: Bucket [{#BUCKETNAME}]: SSE status has changed|change(/Backblaze B2/b2.bucket.sse[{#BUCKETNAME}])<>0|Information|
|B2: Bucket [{#BUCKETNAME}]: Type has changed|change(/Backblaze B2/b2.bucket.type[{#BUCKETNAME}])<>0|Information|
