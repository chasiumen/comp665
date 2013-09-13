#!/usr/bin/python
#add users on LDAP
import sys, re, subprocess
#fname = "Yukari"
#lname = "Aoyama"
#group = "avalanche"

ldif_temp ="/home/morinor/comp665/lab7/ldif_temp"
modify_temp = "/home/morinor/comp665/lab7/modify_temp"
search_last_uid= 'ldapsearch -x -b "ou=People,dc=comp665" "objectclass=person" -LLL |grep -i uidNumber: | cut -f 2 -d \' \' | sort -nr | head -n 1' 

#FUNCTION: User Input Validation-------------
def validate(x):
	if re.search(r"^[A-Z]([a-z]|[A-Z]|-)+$", x):
		#print x,"[OK]"
		return(x)
	else:
		nerror(x)
def nerror(x):
    print x, "must start with a captial letter and contain only letters and hypens!"
    sys.exit()	
#refine output
def refine(cmd):
	proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
	(x, err) = proc.communicate()
	x = x.strip()
	return x

#Get New UserIDNumer
def get_id_num(cmd):
	last_id_num = refine(cmd)
	uid = int(last_id_num) + 1 
	return uid

#FUNCTION: Create New Username---------------
#------Check UID Availability----------
# return number
# 0 entry add new user
# 1 entry UID1
# 2 entry UID2
# 3 entry UID3
def get_uname(fname):
	fname = fname.lower()
	#check number of user with same uid
	search_uid_num = 'ldapsearch -x -b "ou=People,dc=comp665" "uid=' + fname + '"| grep numEntries: | awk -F: \'{print $2}\' '
	x = refine(search_uid_num)
	if x == 0:
		return fname
	else:
		fname = fname + x
		return fname

#FUNCTION: Group availability--------
def chk_group(group):
	search_gid= 'ldapsearch -x -b "cn=' + group + ',ou=People,dc=comp665" "objectclass=posixgroup" -LLL | grep cn: | awk -F: \'{print $2}\''
	gid_name  = refine(search_gid)
	if gid_name == group:
		return group
	else:
		print "Error! Group \"" + group + "\" does not exist!"
		sys.exit()
def get_gid(group):
	search_gid_num = 'ldapsearch -x -b "cn=' + group + ',ou=People,dc=comp665" "objectclass=posixgroup" -LLL | grep gidNumber: | awk -F: \'{print $2}\''
	gid = refine(search_gid_num)
	return gid

#FUNCTION: Create ldif configuration file------
def ldif_conf(line, x, y, z, i ,j, k):
	if re.search("FNAME", line):
		line = re.sub(ur"FNAME", x, line)
		line = re.sub(ur"LNAME", y, line)
		return line	
	elif re.search("LNAME", line):
		line = re.sub(ur"LNAME", y, line)
		return line
	elif re.search("UNAME", line):
		line = re.sub(ur"UNAME", z, line)
		return line
	elif re.search("UID_NUM", line):
		line = re.sub(ur"UID_NUM", i, line)
		return line
	elif re.search("GID_NUM", line):
		line = re.sub(ur"GID_NUM", j, line)
		return line
	elif re.search("GROUP_NAME", line):
		line = re.sub(ur"GROUP_NAME", k, line)
		return line
	else:
		return line

if len(sys.argv) != 4:
#if len(sys.argv) == 4:
	sys.exit("Error! Usage: ./add_ldap_user FNAME LNAME GROUP")
else:
#-----------------MAIN----------------------------
#-------------Validate Username--------------------
	validate(sys.argv[1])
	validate(sys.argv[2])
	fname = sys.argv[1]
	lname = sys.argv[2]
	group = sys.argv[3]
#1. Find New UserIdNumber
	# last_num +1 = current userIDnumer
	uid_num = get_id_num(search_last_uid)
	uid_num = str(uid_num)
	#print "UID(#):", uid_num
#2.	Check user Availibility
	uname = get_uname(fname)
	#print "UID:", uname
#3. Group check
	#Group name
	gname = chk_group(group)
	#print "GID:", gname
	#Group ID
	gid	= get_gid(group)
	gid = str(gid)
	#print "GID(#)", gid 
#4.	add user on the local system
	useradd = 'sudo useradd -d /home/' + uname + ' -c "' + fname + ' ' + lname + '" -g ' + gname +  ' -m -s /bin/bash -u ' + uid_num  + ' ' + uname + ''
	subprocess.call(useradd, shell=True)

#5. add user on LDAP database
	ldif_out = "/home/morinor/comp665/lab7/" + uname +".ldif"
	try:
		#open ldif_temp /read only
		fin = open(ldif_temp, "r")
		#open ldif_out /write only
		fout =open(ldif_out, "w")
	except IOError:
		print "couldn't open", ldif_temp
		sys.exit()
	#read/write
	line = fin.readline()
	while line:
		out = ldif_conf(line, fname, lname, uname, uid_num, gid, gname)
		fout.write(out)
		line = fin.readline()
	fin.close()
	fout.close()
#add User with LDIF
	ldif = 'ldapadd -x -D "cn=Directory Manager" -W -f ' + uname + '.ldif'
	subprocess.call([ldif], shell=True)
#6. modify group
	modify_out = "/home/morinor/comp665/lab7/modify_" + uname + ".ldif"
	try:
		#open ldif_temp /read only
		fin = open(modify_temp, "r")
		#open ldif_out /write only
		fout =open(modify_out, "w")
	except IOError:
		print "couldn't open", modify_temp
		sys.exit()
	#read/write
	line = fin.readline()
	while line:
		out = ldif_conf(line, fname, lname, uname, uid_num, gid, gname)
		fout.write(out)
		line = fin.readline()
	fin.close()
	fout.close()
#modify 
	modify = 'ldapmodify -x -D "cn=Directory Manager" -W -f modify_' + uname + '.ldif'
	subprocess.call([modify], shell=True)
