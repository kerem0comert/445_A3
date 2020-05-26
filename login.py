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
printHeader("KIS Login")  


form = cgi.FieldStorage()

if 'username' in form.keys() and 'pwd' in form.keys():
   print ("Login successful with username = {}, password = {}."
         .format(cgi.escape(form['username'].value),cgi.escape(form['pwd'].value)))
   print("login success")
   redirectURL = localhost/445_A3/login.html
   print('<html>')
   print('  <head>')
   print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
   print('  </head>')
   print('</html>')
elif 'register' in form:
   print("register")