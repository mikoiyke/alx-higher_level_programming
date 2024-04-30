#!/bin/bash
#GET request to the URL and display the response body (if status code is 200)
curl -s -w "%{http_code}" -o /dev/null $1
