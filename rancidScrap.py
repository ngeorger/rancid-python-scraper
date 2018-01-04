#!/usr/bin/python
# -*- coding: utf-8 -*-
# Intellicore 2017 - Nicolas Georger
import urllib2
import base64
import time
import os.path

timestr = time.strftime("%Y%m%d-%H%M%S")
print timestr

username = "user"
password = "pass"
#The URL given by webcvs on rancid, direct to router.db, use your own
request = urllib2.Request("http://localhost/cgi-bin/cvsweb.cgi/~checkout~/acceso/router.db")

#Encoding for the login
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(request)

#In case you want to print on screen the result, uncomment the following line
#print response.read()

# file-output
filepath = "/your/own/desired/path/"
#Generates a file with the current date and gives a cvs extension
x = filepath + timestr
f = open("%s.cvs" % x, "w")
imprimir = response.read()
f.write (imprimir)
f.close()

#End of script
print "Script ran correctly. Check your path for the output"
