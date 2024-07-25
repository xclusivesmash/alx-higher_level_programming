#!/bin/bash
# displays HTTP methods accepted by server.
curl -s -I "$1" | grep "Allow" | cut -d " " -f 2-
