#!/usr/bin/python3
"""
Module: 8-json_api
Description: sends a POST request to http://0.0.0.0:5000/search_user
"""
import sys
import requests


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        q = ""
    else:
        q = args[1]
    payload = {"q": q}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
