#!/bin/bash
# Sends request to a url and only displays the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
