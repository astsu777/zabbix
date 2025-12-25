# Introduction

This template checks if a network mount point is actually mounted or not and returns a numerical value.

## Installation

N/A

## Macros

N/A

## Value Mappings

A simple value mapping is configured for the status: 0=Mounted, else Not mounted.


## Template Links

N/A

## Discovery Rules

The following discovery rule is configured:

|Name|Description|Key|Filters|
|----|-----------|---|-------|
|Discover Network filesystems|Checks what CIFS/NFS/FUSE network mounts are configured|vfs.fs.discovery|^(nfs|nfs4|cifs|fuse)$|


## Items

The following item prototype is configured:

|Name|Description|Key
|----|-----------|---
|Network filesystem status: {#FSNAME}|-|system.run[findmnt -nr -o source -T "{#FSNAME}" > /dev/null && echo 0]|


## Triggers

The following trigger prototype is configured:

|Name|Description|Expression|Priority|
|----|-----------|----------|--------|
|Network filesystem {#FSNAME} is not mounted|-|last(/Linux Network Mount/system.run[findmnt -nr -o source -T "{#FSNAME}" > /dev/null && echo 0])=1|High|


## Graphs

N/A

## Dashboards

N/A
