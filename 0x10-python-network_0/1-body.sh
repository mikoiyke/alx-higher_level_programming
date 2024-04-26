#!/bin/bash
#GET request to the URL and display the response body (if status code is 200)
	curl -s -w "\n%{http_code}" "$1" | awk 'END {if ($NF == 200) print $0}'
