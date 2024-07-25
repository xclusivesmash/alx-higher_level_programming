#!/bin/bash
# sends a request to a url and display the size of body
curl -s "$1" | wc -c
