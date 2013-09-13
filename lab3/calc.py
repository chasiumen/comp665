#!/usr/bin/python

import sys

def cal(x,op,y):
    #print x, op, y
    if op == "plus":
        result = x + y
        print x, op, y ,"is", result
    
    elif op == "minus":
        result = x - y
        print x, op, y ,"is", result    	

    elif op == "times":
        result = x * y
        print x, op, y ,"is", result

    elif op == "over":
        result = x / y
        print x, op, y ,"is", result
    
    elif op == "pow":
        result = x ** y
        print x, op, y ,"is", result
    else:
        print "Error: ",op," is unacceptable operation!"
        sys.exit()


if len(sys.argv) == 4:
    #print sys.argv
    cal(float(sys.argv[1]), sys.argv[2], float(sys.argv[3]) )

else:
    print "usage: ./calc.py num1 op num2"


