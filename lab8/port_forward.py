#!/usr/bin/python
#add new port forwarding rules on iptables
import sys, re, subprocess

#Function: check port# and service name
def	port(x, proto):
	if re.search(r"^\d+$", x):
		if int(x) > 0 and int(x) <= 65535:
			#print "port#:",x
			return x
		else:
			print "Error: invalid port range", x
			sys.exit()
	else:
	#search port number from /etc/services
		dir = "/etc/services"
		try:
			fin = open(dir, "r")
		except IOError:
			print "Couldn't open", dir
			sys.exit()
		line = fin.readline()
		while line:
			s=service(line, x, proto)
			if not (s is None):
				break
			line = fin.readline()
		fin.close()
		return s

def service(line, s_name, proto):
		search = "^"  + s_name + "\s+\d+/" + proto
		if re.search(search, line):
			line = re.split("\s+", line)
			line = re.split("/",line [1])
			return line[0]
	
#Function: check tcp/udp input
def tcp_udp(x):
	if x == "tcp" or x == "TCP":
		#print "ok", x
		x = x.lower()
		return x
	elif x == "udp" or x == "UDP":
		#print "ok", x
		x = x.lower()
		return x
	else:
		print "Error: invalid protocol type [tcp/udp]"
		sys.exit()
#Function: check IP address
def ip_addr(x):
	if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", x):
		return x
	else:
		print "Error! Not a vaid IP address"
		sys.exit()

#-------------------MAIN--------------------------
#check number of argument
if len(sys.argv) != 4:
	print "./port_forward.py port#/service_name protocol_type[tcp/udp] destination_IP_addr"
	sys.exit()
else:
#check tcp/udp
	proto = tcp_udp(sys.argv[2])
#check port# and service name
	port = port(sys.argv[1], proto)
	if not (port is None):
		#print "port:", port
		pass
	else:
		print "port name", sys.argv[1], "not found in /etc/services"
		sys.exit()
#check destination IP address
	ip = ip_addr(sys.argv[3])
	#print "proto:" , proto
#insert rules on iptables
	prerouting = 'iptables -t nat -I PREROUTING -i eth0 -p ' + proto + ' -m ' + proto + ' --dport ' + port + ' -j DNAT --to-destination ' + ip
	foward = 'iptables -I FORWARD -i eth0 -p ' + proto + ' -m ' + proto + ' --dport ' + port + ' -j ACCEPT'
	renew = 'iptables-save > /etc/sysconfig/iptables'
	#print prerouting
	#print foward
	subprocess.call([prerouting], shell=True)
	subprocess.call([foward], shell=True)
	subprocess.call([renew], shell=True)

