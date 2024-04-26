#!/bin/bash
# sends a request to that URL, and displays the size of the body
curl -sS "$1" | awk 'NR==1 {if ($1 == 200) print}'
