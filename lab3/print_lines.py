#!/usr/bin/python

import sys

if len(sys.argv) != 4:
    print "usage: print_lines.py start_line stop_line file"
    sys.exit()

start = int(sys.argv[1])
end = int(sys.argv[2])


if end < start:
    print "start_line must be <= to stop_line"
    sys.exit()


else:
    try:
        file = open(sys.argv[3], "r")
        line = file.readline()
    except IOError:
        print "could'nt open", sys.argv[3]
        sys.exit()

    count = 1
    while line:
        if count >= start and count <= end:
            line = line.rstrip("\n")
            print line
            line = file.readline()
            count+=1
        else:
            count+=1
            line = file.readline()
    if count < start or count < end:
        print "ran out of lines stoping at line", count
    file.close()
