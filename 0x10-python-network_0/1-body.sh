#!/bin/bash
# Sends a GET request and destroys the body of the response
curl -X GET -sL "$1"
