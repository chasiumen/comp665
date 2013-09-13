#!/usr/bin/python

import sys, re, os, subprocess

uname = "tifa"

cmd = 'ldapsearch -x -b "ou=People,dc=comp665" "objectclass=person" -LLL |grep -i uidNumber: | cut -f 2 -d \' \' | sort -nr | head -n 1'

cmd1 = 'ldapsearch -x -b "cn=Avalanche,ou=People,dc=comp665" "objectclass=posixgroup"' 
cmd2 = 'ldapsearch -x -b "ou=People,dc=comp665" "uid=' + uname + '"' + '| grep numEntries: | awk -F: \'{print $2}\''

uname = "yukari"
fname = "Yukari"
lname = "Aoyama"
gname = "avalanche"
uid_num ="5002"


useradd = 'useradd -d /home/' + uname + ' -c "' + fname + ' ' + lname + '" -g ' + gname +  ' -m -s /bin/bash -u ' + uid_num  + ' ' + uname + ''

print useradd + "[end]"
