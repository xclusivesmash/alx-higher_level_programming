#!/usr/bin/python3
"""
Module: 5-hbtn_header
Description: displays the value of the variable X-Request-Id
"""
import sys
import requests


if __name__ == "__main__":
    args = sys.argv
    # get url
    URL = args[1]
    response = requests.get(URL)
    print(response.headers["X-Request-Id"])
