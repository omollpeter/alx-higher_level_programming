#!/bin/bash
# Sends a request to url and displays the size of the body response
curl -sI "$1" | grep "Content-Length" | cut -f2 -d" "
