#!C:\Program Files\Python36\python.exe

import os
import cgi

def printHeader( title ):
   print ("""Content-type: text/html

<?xml version = "1.0" encoding = "UTF-8"?
<!DOCTYPE html PUBLIC
	"-//W3C//DTD XHTML 1.0 Strict//EN"
	"DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
<head><title>%s</title></head>
<body>""" % title) 
printHeader("KIS - Register")  

form = cgi.FieldStorage()

#database has to be checked for the uniquness of the username
if 'register' in form and and 'username' in form.keys() and 'pwd' in form.keys()