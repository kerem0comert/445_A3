#!C:\Program Files\Python36\python.exe
import os
import cgi
import random
import http.cookies as Cookie  
from htmlMethods import *
from database import *

form = cgi.FieldStorage()

if not form or not 'login' in form:
   htmlMethods.printHeader("Login")
   print("""<p>Welcome to Kalkanli Internship System!</p>
        <form method='POST' action='login.py'>
            <label for="username">Username:</label>
            <input type='text' name='username' required/><br><br>
            <label for="pwd">Password:</label>
            <input type='password' name='pwd' required/><br><br>
            <input type='submit' value='Login' name='login' />
        </form>
        <input type="submit" value="I don't have an account" onclick="window.location='register.py';"/>""")
   htmlMethods.endBodyAndHtml()
else:
   if 'login' in form and 'username' in form.keys() and 'pwd' in form.keys():
      sessionID = Database().login(form["username"].value, form["pwd"].value)
      if sessionID == 0:
         htmlMethods.printHeader("Login Failed!")
         print("<p>Login Failed!</p>")
         print("<p>Incorrect username and password</p>")
         print("""<input type="submit" value="Go back" onclick="window.location='login.py';"/>""")
         htmlMethods.endBodyAndHtml()
      else:
         cookie = Cookie.SimpleCookie()
         sessionID = random.randint(1,1000000000)
         cookie["session"] = sessionID
         cookie["session"]["domain"] = "localhost"
         cookie["session"]["path"] = "/"
         isLoginNotSuccessful = Database().updateSessionID(form["username"].value, sessionID)
         if isLoginNotSuccessful:
            htmlMethods.printHeader("Login Failed!")
            print("<p>Login Failed!</p>")
            print("<p>Something went wrong</p>")
            print("""<input type="submit" value="Go back" onclick="window.location='login.py';"/>""")
            htmlMethods.endBodyAndHtml()
         else:
            session_cookie = cookie.output().replace("Set-Cookie: ", "")
            htmlMethods.printHeader("Login Successful!")
            print ("<script>")
            print ("document.cookie = '%s';" % session_cookie)
            print ("window.location = 'index.py';")
            print ("</script>")
            htmlMethods.endBodyAndHtml()
  
