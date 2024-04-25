#!/bin/bash
# Sends GET request with a header to url
curl -X GET -s -H "X-School-User-Id: 98" "$1"
