#!/usr/bin/python

import sys
import re

def filter(x):
    line = sys.stdin.readlines()
    for out in line:
        out = out.rstrip("\n")
        regex='^'+x
        if re.search(regex, out):
            out = re.split(r"\s+", out)
            print out[1],
            for i in range(7,len(out)):
                print out[i],
                if i+1 == len(out):
                    print ""

if len(sys.argv) == 2:
    filter(sys.argv[1])

elif len(sys.argv) == 1:
    filter("morinor")

else:
     print "Error! Usage: psfilter.py [username]"

