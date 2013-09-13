#!/usr/bin/python
#puppet module checker
import sys, os ,re, subprocess

#puppet module directory
dir = '/etc/puppet/modules/'
cmd = 'find /etc/puppet/modules -iname \'*.pp\''

#Function: find source file exist
def ex_source(path, dir):
	#check path is not null
	if not path:
		pass
	else:		
		#open *.pp file
		try:
			fin = open(path, "r")
		except IOError:
			print "Couldn't open file", path
			sys.exit()
		print "Checking manifest", path + "...",
		#convert source path to conf dir path
		line = fin.readline()
		while line:
			if re.search(ur"\s+source\s+", line):
				line = re.split(r"\'", line)
				#puppet:///modules/* => /etc/puppet/modules/*
				line = re.sub("puppet:///modules/", dir, line[1])
				line = re.split(r'/', line)
				#finalize conf dir path		../SERVICE/*.conf => ../SERVICE/files/*.config
				conf = dir + line[4] + "/files/" + line[5]
				#check regular file
				chk(conf)
			line = fin.readline()
		print "done."
	
#check if regualr file exists
def chk(path):
	test = os.path.isfile(path)
	if test == True:
		pass
	else:
		print "\n\tWarning:", path, "not found!",


#-----------------MAIN------------------------
#check number of arguemnt
if len(sys.argv) != 1:
	print "Error! This script does not take any arguments"
	print "usage: ./puppet_module_checker"
	sys.exit()
else: 
#find .pp files
	proc  = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	(r, err) = proc.communicate()
	#store all .pp dir in to an array
	rdir = r.split("\n")
	for line in rdir:
		ex_source(line, dir)
	#	print "LINE:" + line
