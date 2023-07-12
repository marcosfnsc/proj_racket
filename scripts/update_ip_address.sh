#!/bin/env bash

set -o errexit

ip_address=$(ip addr | grep "inet " | grep -Eo "([0-9]+\.){3}[0-9]+" | head -2 | tail -1)
echo "ip=$ip_address:5173"

sed "33s/WebSocket(.*)/WebSocket('ws:\/\/$ip_address:8000')/" -i racket_ui/main.js
