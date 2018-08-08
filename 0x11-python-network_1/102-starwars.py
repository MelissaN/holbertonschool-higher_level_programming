#!/usr/bin/python3
"""
given letter pattern as param to be search val of request; print Star War names
usage: ./101-starwars.py [letter pattern to match names]
"""
from sys import argv
import requests

if __name__ == '__main__':
    if len(argv) < 2:
        pattern = ""
    else:
        pattern = argv[1]
    url = 'https://swapi.co/api/people/?search={}'.format(pattern)
    r = requests.get(url)
    print('Number of results: {}'.format(r.json().get('count')))

    if r.json().get('count') > 0:
        matching_names = r.json().get('results')
        for person in matching_names:
            print(person.get('name'))
            for film in person.get('films'):
                f = requests.get(film)
                print('\t{}'.format(f.json().get('title')))

        more = r.json().get('next')
        page = 2
        while more is not None:
            url = 'https://swapi.co/api/people/?search={}&page={}'.format(
                pattern, page)
            r = requests.get(url)
            matching_names = r.json().get('results')
            for person in matching_names:
                print(person.get('name'))
                for film in person.get('films'):
                    f = requests.get(film)
                    print('\t{}'.format(f.json().get('title')))
            more = r.json().get('next')
            page += 1
