#!/usr/bin/python3
"""
given repo and owner name as argvs, use Github API to list last 10 commits
usage: ./100-github_commits.py [github_repo] [github_owner]
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    r = requests.get(url)
    list_commits = r.json()
    for commit in list_commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
