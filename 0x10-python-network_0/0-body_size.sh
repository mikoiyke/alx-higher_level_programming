#!/bin/bash
response=$(curl -sS "$1")
echo "$response" | wc -c
