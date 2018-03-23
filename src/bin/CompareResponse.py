#!/usr/bin/env python

import json
import sys


def compare_json_data(source_data_a, source_data_b):
    def compare(data_a, data_b):
        # type: list
        if (type(data_a) is list):
            # is [data_b] a list and of same length as [data_a]?
            if ((type(data_b) != list) or (len(data_a) != len(data_b))):
                return False

            # iterate over list items
            for list_index, list_item in enumerate(data_a):
                # compare [data_a] list item against [data_b] at index
                if (not compare(list_item, data_b[list_index])):
                    return False

            # list identical
            return True

        if (type(data_a) is tuple):
        	# is [data_b] a tuple and of same length as [data_a]?
        	if ((type(data_b) != tuple) or (len(data_a) != len(data_b))):
        		return False
        
        	# iterate over tuple items
        	for tuple_index,tuple_item in enumerate(data_a):
        		# compare [data_a] tuple item against [data_b] at index
        		if (not compare(tuple_item,data_b[tuple_index])):
        			return False
        
        	# tuple identical
        	return True

        # type: dictionary
        if (type(data_a) is dict):
            # is [data_b] a dictionary?
            if (type(data_b) != dict):
                return False

            # iterate over dictionary keys
            for dict_key, dict_value in data_a.items():
                # key exists in [data_b] dictionary, and same value?
                if ((dict_key not in data_b) or (not compare(dict_value, data_b[dict_key]))):
                    return False

            # dictionary identical
            return True

        # simple value - compare both value and type for equality
        if (data_a == data_b) and (type(data_a) is type(data_b)):
            return True
        else:
            errorStr = (str(data_a) + ' is different from ' + str(data_b))
            appendToFile('../reports/error.log', errorStr)
            noError = False
            return False
			
    # compare a to b
    return (compare(source_data_a, source_data_b))


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def load_json(file_path):
    # open JSON file and parse contents
    fh = open(file_path, 'r')
    data = json.load(fh)
    fh.close()
    data = ordered(data)
    return data


def appendToFile(file_path, obj):
    orig_stdout = sys.stdout
    with open(file_path, 'a') as file:
        sys.stdout = file
        print(obj)
        sys.stdout = orig_stdout
    file.close()


def compareOutputs():
    # import testing JSON files to Python structures
    a_json = load_json('../reports/response1.json')
    b_json = load_json('../reports/response2.json')

    # compare first struct against second
    return compare_json_data(a_json, b_json)
