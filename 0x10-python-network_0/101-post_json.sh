#!/bin/bash
# Sends post request with json data
curl -X POST -s -H "Content-Type: application/json" -d "$2" "$1"
