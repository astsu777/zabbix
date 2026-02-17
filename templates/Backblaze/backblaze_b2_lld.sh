#!/usr/bin/env bash
#=========================================================================
# Author: Gaetan (gaetan@ictpourtous.com) - Twitter: @astsu777
# Creation: Tue 17 Feb 2026 13:57:43
# Last modified: Tue 17 Feb 2026 13:58:11
# Version: 1.0
#
# Description: Retrieve useful data from Backblaze B2 buckets
#=========================================================================

if [ "$1" == "discover" ]; then
    /usr/bin/backblaze-b2 list-buckets --json | jq -c '[ .[] | { bucketName: .bucketName, bucketId: .bucketId, bucketType: .bucketType, encryption: .defaultServerSideEncryption.mode, fileLock: .isFileLockEnabled } ]'
    exit 0
fi

# If a field and bucket name are given
FIELD=$1
BUCKET=$2

if [ ! -z "$FIELD" ] && [ ! -z "$BUCKET" ]; then
    DATA=$(/usr/bin/backblaze-b2 get-bucket "$BUCKET" --show-size)

    case "$FIELD" in
        size) jq -r '.totalSize' <<<"$DATA" ;;
        filecount) jq -r '.fileCount' <<<"$DATA" ;;
        type) jq -r '.bucketType' <<<"$DATA" ;;
        encryption) jq -r '.defaultServerSideEncryption.mode' <<<"$DATA" ;;
        id) jq -r '.bucketId' <<<"$DATA" ;;
        filelock) jq -r '.isFileLockEnabled' <<<"$DATA" ;;
        *) echo "Unknown field" >&2; exit 1 ;;
    esac

    exit 0
fi

echo "Usage: $0 discover | <field> <bucketname>"
exit 1
