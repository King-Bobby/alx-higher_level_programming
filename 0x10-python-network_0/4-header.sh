#!/bin/bash
# take in URL, A header variable X-School-User-Id must be sent with the value 98, display body response
curl -s -H "X-School-User-Id":98 "$1"
