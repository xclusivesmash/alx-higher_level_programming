#!/usr/bin/python3
"""
Module: 1-hbtn_header
Description: send a request to a URL and display
the value of the X-Request-Id variable in the
header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    args = sys.argv
    URL = args[1]
    request = urllib.request.Request(URL)
    with urllib.request.urlopen(request) as f:
        # use reponse
        response = dict(f.headers).get(("X-Request-Id"))
        print(response)
