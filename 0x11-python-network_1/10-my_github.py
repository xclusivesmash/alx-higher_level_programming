#!/usr/bin/python3
"""
Module: 10-my_github
Description: takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    args = sys.argv
    one = args[1]
    two = args[2]
    auth = HTTPBasicAuth(one, two)
    r = requests.get("https://api.github.com/user", auth=auth)
    response = r.json().get("id")
    print(response)
