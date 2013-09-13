#!/usr/bin/python
#midterm takehome test 2
#Fibonacci squence
#F(n+2)=F(n)+F(n+1)
#1,1,2,3,5,8,13,21,34,55....
#F(n) = F(n-1)+F(n-2)

import sys

#fibonacci squence
def fib(n):
	if n < 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

if len(sys.argv) != 2:
	print "usage: fib.py N"
	sys.exit()
else:
	#check N
	if int(sys.argv[1]) < 1:
		print "N must be at least 1"
	else:
		for i in range(int(sys.argv[1])):	
			print fib(i)
		
