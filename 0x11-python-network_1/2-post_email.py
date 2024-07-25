#!/usr/bin/python3
"""
Module: 2-post_email
Description: sends a POST request to passed URL
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    args = sys.argv
    # get url
    URL = args[1]
    # get email
    email = args[2]
    values = {"email": email}
    data = urllib.parse.urlencode(values).encode("utf-8")
    request = urllib.request.Request(URL, data)
    with urllib.request.urlopen(request) as f:
        # use response
        response = f.read().decode("utf-8")
        print(response)
