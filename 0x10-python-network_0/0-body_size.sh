#!/bin/bash
# send a request to an URL with curl, and displays the size of the body of the response
curl -sI "$1" | awk '/Content-Length/{print $2}'
