#!/usr/bin/python3
"""
Module: 0-hbtn_status
Description: Fetches a url on the web.
"""
import urllib.request


if __name__ == "__main__":
    URL = "https://alx-intranet.hbtn.io/status"
    request = urllib.request.Request(URL)
    with urllib.request.urlopen(f"{request}") as f:
        response = f.read()
        # print(response)
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode("utf-8")))
