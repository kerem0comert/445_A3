#!C:\Program Files\Python36\python.exe
import os
import cgi
from htmlMethods import *
from database import *

form = cgi.FieldStorage()
dbConnection = Database()

if 'login' in form and 'username' in form.keys() and 'pwd' in form.keys():
   sessionID = dbConnection.login(form["username"].value, form["pwd"].value)
   if not sessionID:
      htmlMethods.printHeader("Login Failed!")
      print("<p>Login Failed!</p>")
      print("<p>Incorrect username and password</p>")
      print("""<input type="submit" value="Go back" onclick="window.location='login.html';"/>""")
      htmlMethods.endBodyAndHtml()
  
