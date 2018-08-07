#!/usr/bin/python3
"""
given letter pattern as param to be search val of request; print Star War names
usage: ./9-starwars.py [letter pattern to match names]
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://swapi.co/api/people'
    param = {'search': argv[1]}
    r = requests.get(url, params=param)

    matching_ppl = r.json()
    print("Number of results: {}".format(matching_ppl.get('count')))
    for person in matching_ppl.get('results'):
        print(person.get('name'))
