#!/usr/bin/python

import sys, re, subprocess, os

if len(sys.argv) != 1:
     print "Usage: ./get_external_ip.py"
else:
    fchk = os.path.exists("./index.html")
    
    if fchk:
        os.remove("./index.html")
    
    subprocess.call("wget -q www.ipchicken.com", shell=True)
    
    try:
        file = open("./index.html", "r")
        text = file.read()
    except IOError:
        print "couldn't open a file"
        sys.exit()
    
    out = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", text)
    print out[0]
    os.remove("./index.html")
    file.close() 
