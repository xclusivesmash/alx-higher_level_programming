#!/usr/bin/python3
"""
Module: 7-error_code
Description: sends a request to the URL
"""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    # get URL
    URL = args[1]
    response = requests.get(URL)
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.text)
