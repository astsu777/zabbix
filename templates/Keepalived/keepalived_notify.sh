#!/usr/bin/env sh
#=========================================================================
# Author: Gaetan (gaetan@ictpourtous.com) - Twitter: @GaetanICT
# Creation: Tue 09 Dec 2025 19:51:07
# Last modified: Tue 09 Dec 2025 19:59:38
# Version: 1.0
#
# Description: Write VRRP instance to a file so it can be monitored
# The status will be updated using the 'notify' in 'keepalived.conf'
#=========================================================================

#=======================
# VARIABLES
#=======================

STATUSFILE="/run/keepalived_status"

#=======================
# RUN
#=======================

touch "$STATUSFILE"
chmod 0644 "$STATUSFILE"
echo "$1 $2 has transitioned to the $3 state with a priority of $4" > "$STATUSFILE"
