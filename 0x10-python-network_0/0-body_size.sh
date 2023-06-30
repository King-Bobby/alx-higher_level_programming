#!/bin/bash
# Script takes URL, sends request and displays Content length of response
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
