#!/usr/bin/python3
"""
given URL & email as params, display response body utf-8, print error codes
usage: ./3-error_code.py http://0.0.0.0:5000/status_401
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
