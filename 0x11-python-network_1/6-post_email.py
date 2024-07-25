#!/usr/bin/python3
"""
Module: 6-post_email
Description: sends a POST request to the passed URL
"""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    # get url
    URL = args[1]
    # get email
    email = args[2]
    # set up value ad dict
    value = {"email": email}
    response = requests.post(URL, data=value)
    print(response.text)
