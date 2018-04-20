#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is not None:
        while value in a_dictionary.values():
            for key in a_dictionary.keys():
                if a_dictionary[key] == value:
                    del a_dictionary[key]
                    break
        return(a_dictionary)
