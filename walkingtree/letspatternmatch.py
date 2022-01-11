#!/usr/bin/env python3
## Script to search for a pattern match
import os, fnmatch

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg ")
lookwhere = input("What is the path in which I should search? ")

print(find(lookfor, lookwhere))

