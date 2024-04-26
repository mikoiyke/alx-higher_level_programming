#!/bin/bash
# sends a request to that URL, and displays the size of the body
curl -sSL "$1" | awk 'NR==1 && $1 == 200'
