#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successful = 0 # total times we see pattern, "-] Authorization failed"

# open the file for reading
with open("/home/student/2022-01-04-Python/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
        #elfi- success pattern
        elif "-] Authorization failed" in line:
            successful += 1 
#display the number of failed log in attempts
print("The number of failed log in attempts is", loginfail)

#display the number of successful log in attempts
print("The number of successful log ins is", successful)
