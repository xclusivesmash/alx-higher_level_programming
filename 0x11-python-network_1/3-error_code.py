#!/usr/bin/python3
"""
Module: 3-error_code
Description: sends a request to URL and returns body
of the response.
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    args = sys.argv
    # get url
    URL = args[1]
    request = urllib.request.Request(URL)
    try:
        with urllib.request.urlopen(request) as f:
            response = f.read().decode("utf-8")
            print(response)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e))
