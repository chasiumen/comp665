#!/usr/bin/python

import sys
import re

def chkname(x, y):
    if re.search(r"^[A-Z]([a-z]|[A-Z]|-)+$", y):
        return(x, y)
    else:
        nerror(x)

def chkzip(x, y):
    if re.search(r"^(\d){5}$", y):
        return(x, y)
    else:
        print x,"must be exactly 5 digits!"
        sys.exit()

def chkadd(x, y):
    if re.search(r"^(\d|\w|\.|-)+@(\d|\w|\.|-)+.(\d|\w|\.|-)+$", y):
        print "Validated!"
        return(x, y)
    else:
        print x,"must be USER\@DOMAIN, where both USER and DOMAIN must be only letters, numbers, dots, underscores, and hyphens!"
        sys.exit()

def nerror(x):
    print x, "must start with a captial letter and contain only letters and hypens!"
    sys.exit()



if len(sys.argv) != 1:
    print "usage: ./validate.py"
else:
    input = raw_input("First name: ")
    chkname("First name", input)

    input = raw_input("Last name: ")
    chkname("Last name", input)
    
    input = raw_input("Zip code: ")
    chkzip("Zip Code", input)

    input = raw_input("Email Address: ")
    chkadd("Email Address", input)

