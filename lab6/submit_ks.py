#!/usr/bin/python
#kickstart
import sys, re

ks_temp="/export/centos64/template.ks.cfg"
pxe_temp="/tftpboot/pxelinux.cfg/template"


#---------------------FUNCTION------------------------
def	ks_conf(x, y):
	if re.search("CHANGE_HOST_NAME", x):
		x = re.sub(ur"CHANGE_HOST_NAME", y, x )
		return x
	else:
		return x
def pxe_conf(x, y):
	if re.search("KS_CONF", x):
		x = re.sub(ur"KS_CONF", y, x)
		return x
	else:
		return x
def fix(x):
	x = re.sub(":", "-", x)
	x = x.lower()
	return x	
#-----------------------MAIN--------------------------
#check number of arguments
if len(sys.argv) != 3:
	print "ERROR! Usage: ks.py HOST_NAME ETH_ADDR"
	sys.exit()
else:
	#validate MAC
	if re.search(u"^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$", sys.argv[2]):
		#print "VALID!"
		addr = fix(sys.argv[2])
	else:
		print "Error! Not valid physical address [", sys.argv[2], "]"
		sys.exit()
	
	ks_out="/export/centos64/" + sys.argv[1] + ".ks.cfg"
	pxe_out="/tftpboot/pxelinux.cfg/01-" + addr

#---------------------ks CONFIG-----------------------
	try:
		#open ks temp file /read-only
		fin = open(ks_temp, "r")
		#open ks output file /write-only
		fout = open(ks_out, "w")		
	except IOError:
		print "couldn't open", ks_temp
		sys.exit()
	#read/write
	line = fin.readline()
	while line:
		out  = ks_conf(line, sys.argv[1])	
		fout.write(out)
		line = fin.readline()		
	fin.close()
	fout.close()
#---------------------PXE CONFIG---------------------
	try:
		#open pxe temp file /read-only
		fin = open(pxe_temp, "r")
		#open pxe  output file /write-only
		fout = open(pxe_out, "w")		
	except IOError:
		print "couldn't open", pxe_temp
		sys.exit()
	#read/write
	line = fin.readline()
	while line:
		out  = pxe_conf(line, sys.argv[1])
		fout.write(out)
		line = fin.readline()		
	fin.close()
	fout.close()
