#!/bin/bash
# displays HTTP methods accepted by server.
curl -s -iL -X OPTIONS "$1"
