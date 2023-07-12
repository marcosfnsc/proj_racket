#!/bin/env bash

set -o errexit

sed "33s/WebSocket(.*)/WebSocket('ws:\/\/localhost:8000')/" -i racket_ui/main.js
