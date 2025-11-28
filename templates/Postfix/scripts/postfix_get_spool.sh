#!/bin/bash
postfix_config=/etc/postfix/main.cf
basedir=$(grep -e ^queue_directory $postfix_config | sed 's/.\+=[[:space:]]\?\(.\+\)/\1/')
[[ $basedir ]] || basedir=/var/spool/postfix  # Fallback to default when not found in config
queuedirs="deferred active maildrop incoming corrupt hold"

idx=0
echo -n '{'
for dir in $queuedirs; do
    [[ $idx != 0 ]] && echo -n ","
    echo -n "\"$dir\":"
    if [ -r $basedir/$dir ]; then
        echo -n $(find "$basedir/$dir" -type f | wc -l)
    else
        echo -n "-1"
    fi
    idx+=1
done
echo -n '}'
