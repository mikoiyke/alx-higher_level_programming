#!/bin/bash
# displays all HTTP methods the server will accept
curl --head $1 | grep -i allow
