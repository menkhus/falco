#!/usr/bin/env python

""" Uses some code I found on stack overflow, looking for version 
	strings in a binary
"""

import string
import sys
import re

def strings(filename, min=4):
    """ This is essentially the unix strings funcitonality.
        Code was copied from a stack overflow example
    """
    with open(filename, "rb") as f:
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                yield result
            result = ""

def main():
	f = sys.argv[1]
	content = strings(f,4)
	# This is a version string, matches N, N.N or N.N.N
	#version = '(\d+\\.)?(\d+\\.)?(\d+\\.)'
	#print "Searching %s for version information"%(f,)
	#for each in content:
	#if re.search(version,each):
	#		print each
	#print "Searching for IP addresses embedded in: %s"%(f,)
	ipv4addr = '(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})'
	try:
		content = open(f,'rb')
	except:
		exit()
	for each in content:
		addr = re.search(ipv4addr,each)
		if addr:
			print "found IP addresses embedded in: %s"%(f,)
			print "%s.%s.%s.%s"%(addr.groups())

if __name__ == "__main__":
    main()