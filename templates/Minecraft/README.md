# Introduction

This template checks if a Minecraft instance and its accompanying SFTP instance are UP or not.

## Installation

N/A

## Macros

The following macros are configured:

|Name|Value|Description|
|----|-----|-----------|
|{$MINECRAFT.HOST}|{HOST.HOST}|FQDN/IP of the Minecraft server if different from the host|
|{$MINECRAFT.PORT}|25565|TCP port of the Minecraft listener|
|{$MINECRAFT.SFTP.PORT}|22|TCP port of the Minecraft instance SFTP listener|

## Template Links

N/A

## Discovery Rules

N/A


## Items

The following items are configured:

|Name|Type|Key|
|----|----|---|
|Minecraft Service|Simple check|net.tcp.service[tcp,{$MINECRAFT.HOST},{$MINECRAFT.PORT}]|
|Minecraft SFTP Service|Simple check|net.tcp.service[tcp,{$MINECRAFT.HOST},{$MINECRAFT.SFTP.PORT}]|


## Triggers

The following items are configured:

|Name|Expression|Severity|
|----|----------|--------|
|Minecraft instance is DOWN|last(/Minecraft/net.tcp.service[tcp,{$MINECRAFT.HOST},{$MINECRAFT.PORT}],#1)=0|High|
|Minecraft SFTP server is DOWN|last(/Minecraft/net.tcp.service[tcp,{$MINECRAFT.HOST},{$MINECRAFT.SFTP.PORT}],#1)=0|Average|


## Graphs

N/A


## Dashboards

N/A
