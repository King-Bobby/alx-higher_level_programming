#!/bin/bash
# takes in URL, uses POST key:values
curl -s -X POST -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
