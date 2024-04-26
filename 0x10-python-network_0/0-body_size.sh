#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Use curl to fetch the URL and store the response in a temporary file
#temp_file=$(mktemp)
curl -sS "$URL" -o "$temp_file"

# Get the size of the response body in bytes
body_size=$(stat -c %s "$temp_file")

# Display the size of the body in bytes
echo "$body_size"

# Clean up the temporary file
#rm "$temp_file"
