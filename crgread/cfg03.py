#!/usr/bin/env python3v
## create file object in "r"ead mode

filename = input("Name of file: ")

with open(f"{filename}", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
num_lines = len(configlist)
print(f"Using the len() function, we see there are: {num_lines} line")

