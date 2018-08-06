#!/usr/bin/python3
"""
given URL as parameter, fetch URL and display value from reponse header
usage: ./1-hbtn_header https://intranet.hbtn.io
"""
import sys
import urllib.request

URL = sys.argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(URL) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
