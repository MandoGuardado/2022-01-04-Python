#!/usr/bin/env python3
## Script to search and stop on first match
import os

## Define a function that stops searching on first match
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

lookfor = input("What am I looking for? ")
lookwhere = input("What is the path in which I should search? ")

print(find(lookfor, lookwhere))

