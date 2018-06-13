#!/usr/bin/python3

import sys
import cgi, cgitb
import datetime
import time

cgitb.enable()

f = open("guru99.txt","w+")
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
f.write(sys.stdin.read())
f.close()

print ("Content-Type: text/plain\n\r")

print ("<b>We at least, did something.</b>")
