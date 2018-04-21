#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None:
        if key in a_dictionary:
            del a_dictionary[key]
        return a_dictionary

#    return a_dictionary.pop(key, None)
