#!/bin/bash

SERVER="{server}"
PASSWD="{password}"
METHOD="{method}"
PORT="{port}"
RATIO="{ratio}"
EXTRA=$(cat <<EOF
{extra}
EOF)

function start_connection
{{
    sslocal -s $SERVER -p $PORT -l 1080 -k $PASSWD -m $METHOD
}}

function show_connection_info
{{
	echo `date`
    echo "        SERVER: $SERVER"
	echo "        METHOD: METHOD"
	echo "    LOCAL PORT: 1080"
	echo "BANDWITH RATIO: $RATIO"
	echo $EXTRA
	echo "==================================="
}}

show_connection_info
start_connection
