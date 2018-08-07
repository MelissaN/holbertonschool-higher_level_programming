#!/usr/bin/python3
"""
given username and pw as param, get your id from Github api
usage: ./10-my_github.py [github_username] [github_pw]
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
