#!C:\Program Files\Python36\python.exe

import os
import cgi
from htmlMethods import htmlMethods

htmlMethods.printHeader("Kalkanli Internship System")
form = cgi.FieldStorage()

if 'login' in form and 'username' in form.keys() and 'pwd' in form.keys():
   print ("Login successful with username = {}, password = {}."
         .format(cgi.escape(form['username'].value),cgi.escape(form['pwd'].value)))
   print("login success")
   htmlMethods.redirect("login.html")
elif 'register' in form:
   htmlMethods.redirect("register.html")


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




  
