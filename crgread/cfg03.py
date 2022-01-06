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
num_lines= 0
for line in configlist:
    if line.startswith("\n"):
        pass
    else:
        num_lines +=1

print(f"The number of line in the file is: {num_lines}")
