#!/bin/bash
# takes in filename and URL, POST contents of file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
