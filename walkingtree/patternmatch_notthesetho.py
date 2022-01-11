#!/usr/bin/env python3
#Author: RZFeeser RZFeeser@alta3.com

"""Script to search for a pattern match"""

import os # used to walk the system
import fnmatch # for regex pattern matching

EXCLUDE = ["/usr", "/home", "/var"] ## Don't search in these locations


def find(pattern, path):
    """search through filesystem based on given path location"""
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: # if the root matches the exclude list
            dirs[:] = [] # remove the directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in files: # always perform the nested loop, but it maybe empty
            if fnmatch.fnmatch(name, pattern): # if match
                result.append(os.path.join(root, name)) # add to our list
    return result # return the list

def main():
    """runtime code"""
    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    lookwhere = input("What is the path in which I should search? ")
    print("Results: ", find(lookfor, lookwhere)) # call function

main()
 
