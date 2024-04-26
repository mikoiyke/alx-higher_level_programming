#!/usr/bin/bash
# Send a request to the URL and store the response body in a temporary file
response=$(curl -sS "$1")

# Calculate the size of the response body (in bytes)
body_size=$(echo "$response" | wc -c)

# Display the size of the response body
echo "Size of the response body: $body_size bytes"

exit 0
