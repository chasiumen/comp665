#!/usr/bin/python
#add a new users to Asterisk Server
import sys, re, subprocess

#FUNCTION: get ext#
def get_exten(line):
	if re.search(r"exten|EXTEN\s?=>\s?", line):
		#print line
		line = re.split(r"\s?=>\s?",line)
		line = re.split(r",", line[1])
		#store ext# greater than 4001
		if  int(line[0]) >= 4001:
			a_exten.append(int(line[0]))
		else:
			pass
	return a_exten
#FUNCTION: APEEND   
def f_append(dir, new_ext, pin, uname, fullname, email, mode):
	try:
		fin = open(dir, "a")
	except IOError:
		print "couldn't open", dir
		sys.exit()
	#check mode to determain the configuration files
	#sip.conf
	if mode == "sip":
		fin.write("\n[" + uname + "]\ntype=friend\nhost=dynamic\nsecret=" + email + "\ncontext=users\ndisallow=all\nallow=ulaw\nallow=alaw\nallow=gsm\n")
	#extensions.conf
	elif mode == "exten":
		fin.write("\nexten => " + new_ext + ",1,Dial(SIP/" + uname  + " , 20)\n same => n,VoiceMail("+ new_ext + "@user-voicemail, u)\n")
	#voicemail.conf
	elif mode == "voice" :
		fin.write("\n" + new_ext + " => " + pin + "," + fullname + "," + email + "," + email +",attach=yes|tz=eastern\n")	
	else:
		fin.close()
#---------------MAIN-------------------
if len(sys.argv) != 4:
	print "Error! usage: ./add_sip_user.py USERNAME FULLNAME EMAIL"
	sys.exit()
else:
	#set variables
	a_exten = []
	uname = (sys.argv[1]).lower()
	fullname = sys.argv[2]
	email = sys.argv[3]
	#conf file directory
	dir_sip="/etc/asterisk/sip.conf"
	dir_exten="/etc/asterisk/extensions.conf"
	dir_voice ="/etc/asterisk/voicemail.conf"
	#reload commands
	r_sip='sudo asterisk -rx "sip reload"'
	r_exten='sudo asterisk -rx "dialplan reload"'
	r_voice='sudo asterisk -rx "voicemail reload"'

#1. Find lowest extention number
	#open extention.conf and get extension numbers
	try:
		fin = open(dir_exten, "r")
	except IOError:
		print "couldn't open", dir_exten
		sys.exit()
	line = fin.readline()
	while line:
		line=line.strip()
		#funcion get_exten()
		a_exten = get_exten(line)
		line = fin.readline()
	fin.close()
	#next ext#
	a_exten= sorted(a_exten)
 	new_ext = str(a_exten[-1]+1)
	#print "ext#:", new_ext
	#PIN
	pin = new_ext[::-1]
	#print "PIN", pin
#2. Append to sip.conf
	#test = "/home/morinor/comp665/lab10/test.txt"
	#f_append(dir, new_ext, pin, uname, fullname, email, mode)
	f_append(dir_sip, new_ext, pin,  uname, fullname, email, "sip")
#3. Append to extensions.conf
	f_append(dir_exten, new_ext, pin, uname, fullname, email, "exten")
#4. Append to voicemail.conf
	f_append(dir_voice, new_ext, pin, uname, fullname, email, "voice")
#5. reload
	subprocess.call([r_sip], shell=True)
	subprocess.call([r_exten], shell=True)
	subprocess.call([r_voice], shell=True)

	print "Added " + uname + " at " + new_ext + " with PIN " + pin 
