#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body
curl -d $1 $2
