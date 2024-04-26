#!/bin/bash
# sends a request to that URL, and displays the size of the body
curl -sS "$1" | wc -c
