#!C:\Program Files\Python36\python.exe
import os
import cgi
from htmlMethods import *
from database import *

form = cgi.FieldStorage()

if not form or not 'login' in form:
   htmlMethods.printHeader("Login")
   print("""<p>Welcome to Kalkanli Internship System!</p>
        <form method='POST' action='login.py'>
            <label for="username">Username:</label>
            <input type='text' name='username'/><br><br>
            <label for="pwd">Password:</label>
            <input type='password' name='pwd' /><br><br>
            <input type='submit' value='Login' name='login' />
        </form>
        <input type="submit" value="I don't have an account" onclick="window.location='register.py';"/>""")
   htmlMethods.endBodyAndHtml()
else:
   if 'login' in form and 'username' in form.keys() and 'pwd' in form.keys():
      sessionID = Database().login(form["username"].value, form["pwd"].value)
      if not sessionID:
         htmlMethods.printHeader("Login Failed!")
         print("<p>Login Failed!</p>")
         print("<p>Incorrect username and password</p>")
         print("""<input type="submit" value="Go back" onclick="window.location='login.py';"/>""")
         htmlMethods.endBodyAndHtml()
      else:
         htmlMethods.redirect("index.py")
  
