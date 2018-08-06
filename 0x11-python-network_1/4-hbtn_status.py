#!/usr/bin/python3
"""
fetch https://intranet.hbtn.io/status; display response
"""
import requests

if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
