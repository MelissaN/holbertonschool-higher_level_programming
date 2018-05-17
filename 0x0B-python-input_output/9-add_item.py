#!/usr/bin/python3
"""
Module 9-add_item

Contains function that adds and saves to Python obj to JSON file; loads objects

# run with ./9-add_item.py
#
# cat add_item.json ; echo ""
# expect output: []
#
# ./9-add_item.py some random args
# cat add_item.json ; echo ""
# expect output: ["some", "random", "args"]

"""


from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_content = load_from_json_file(filename)
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], filename)
