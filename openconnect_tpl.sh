#!/bin/bash

GROUP=$1
MODE="smart"
SERVER="{server}"
PASSWD="{password}"
USER="{user}"

function start_connection
{{
	echo $PASSWD | sudo openconnect --user=$USER --authgroup=$MODE --passwd-on-stdin $SERVER:4433 
}}

function show_connection_info
{{
	echo `date`
    echo "SERVER: $SERVER"
	echo "  USER: $USER"
}}

function show_message
{{

	echo "==================================="
	show_connection_info
	# no group assigned
	echo "-----------------------------------"

	if [ "$GROUP" == "" ]; then
		echo "RUN WITH GROUP NUMBER:"
		echo "1) smart"
		echo "2) global"
		echo "3) smart-blacklist"
	else
		case $GROUP in
			1)
				MODE="smart"
			;;
			2)
				MODE="global"
			;;
			3)
				MODE="smart-blacklist"
			;;
			*)
				MODE="smart"
		esac
		echo "RUNNING IN [$MODE] MODE"
	fi
	
	echo "==================================="
}}

show_message
start_connection
