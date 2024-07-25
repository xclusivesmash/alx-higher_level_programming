#!/usr/bin/bash
# sends a request to a url and display the size of
# the bdy of the response.
curl -s "$1" | wc -c
