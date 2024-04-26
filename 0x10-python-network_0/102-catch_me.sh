#!/bin/bash
# Sends a request and displays the server response message
curl -X PUT -sL -d 'You got me!' 0.0.0.0:5000/catch_me | grep "Message" | cut -f2 -d\' | sed 's/PUT.*//'
