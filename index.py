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
printHeader("Kalkanli Internship System")  
#print ("<h1>Welcome to the Kalkanli Internship Sytem!</h1>")
#print("""<form method='post' action='index.py'>
#         <input type='text' name='username'/>
#         <input type='text' name='password'/>
#         <input type='submit' value = 'Login' name = 'login'/>
#         <input type='submit' value = "I don't have an account" name = 'register'/>
#         </form>
#         """)  

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


"""
query = os.environ["QUERY_STRING"]    
if len(query) == 0:  
   print (<p><br /> 
      Please add some name-value pairs to the URL above. 
      Or try 
      <a href = "index.py?name=Veronica&age=23">this</a>. 
      </p>)  
else:     
   print (<p style = "font-style: italic"> 
      The query string is '%s'.</p> % cgi.escape(query))  
   pairs = cgi.parse_qs(query)  
     
   for key, value in pairs.items():  
      print ("<p>You set '%s' to value %s</p>" % (key, value))               
print ("</body></html>")"""




  
