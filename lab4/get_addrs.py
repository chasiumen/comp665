#!/usr/bin/python
import sys, re, subprocess, os

file= '/etc/dhcp/dhcpd.conf'
host=[]
mac=[]
ip=[]

def f_host(x):
    if re.search("host", x):
        print "original:", x
        x = re.split(ur"\s*host\s*", x)
        x = re.split(ur"\s*{", x[1])
        print x[0]
        #host.append(x[0])
def f_mac(x):
    if re.search("hardware ethernet", x):
        x = re.split(ur"hardware\s+ethernet", x)
        x = chopper(x)
        #print "MAC",x[0], "[end]"
        if re.search(r"^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$", x[0]):
            #print x[0]
            mac.append(x[0])
        else:
            print "Error: not a valid MAC address"

def f_ip(x):
    if re.search("fixed-address", x):
        x = re.split(ur"fixed-address", x)
        x = chopper(x)
        #print "IP:", x[0],"[end]"
        if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", x[0]):
            #print x[0]  
            ip.append(x[0])
        else:
            print "Error not a vaid IP address"

def chopper(x):
    x = re.split(";", x[1])
    x = re.split(r"\s*", x[0])
    x = re.split(r"\s*$", x[1])
    #print x[0]
    return x

if len(sys.argv) != 1:
    print "Usage: sudo ./get_addr.py"
else:
    fchk = os.path.exists("/etc/dhcp/dhcpd.conf")
    
    if fchk:
        pass
    else:
        "Error: dhcpd.conf does not exist."
        sys.exit()
    try:
        file = open("/etc/dhcp/dhcpd.conf", "r")
        line = file.readline()
    except IOError:
        print "Could'nt open a file"
        sys.exit()
    while line:
        line=line.rstrip("\n")
        f_host(line)
        f_mac(line)
        f_ip(line)
        
        line = file.readline()
 
    #output
    if len(host) != len(mac) or len(mac) != len(ip):
        print "Error: list size does not match "
        sys.exit()
    else:
        for i in range(len(host)):
            print host[i], mac[i], ip[i]

 
