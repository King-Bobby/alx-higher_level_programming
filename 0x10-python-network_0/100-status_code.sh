#!/bin/bash
# takes in URL and displays only status code
curl -o /dev/null -w '%{http_code}' -sLI "$1"
