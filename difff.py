#!/usr/bin/env python

import sys,difflib

textfile1=sys.argv[1]
textfile2=sys.argv[2]

def readfile(filename):
	try:
		filehandle=open(filename,'rb')
		text=filehandle.read().splitlines()
		filehandle.close()
		return text
	except IOError as error:
		sys.exit()
text1=readfile(textfile1)
text2=readfile(textfile2)
d=difflib.HtmlDiff()
print d.make_file(text1,text2)
