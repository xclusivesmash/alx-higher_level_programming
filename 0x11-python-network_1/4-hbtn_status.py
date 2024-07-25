#!/usr/bin/python3
"""
Module: 4-hbtn_status
Description: fetches https://alx-intranet.hbtn.io/status
"""
import request


if __name__ == "__main__":
    URL = "https://alx-intranet.hbtn.io/status"
    response = request.get(URL)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
