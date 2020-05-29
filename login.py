#!C:\Program Files\Python36\python.exe
import os
import cgi
import random
import http.cookies as Cookie  
from htmlMethods import *
from database import *

form = cgi.FieldStorage()

if 'logout' in form:
   htmlMethods.printHeader("Please wait...")
   cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
   sessionID = cookie["session"].value
   Database().updateSessionID(Database().getUsernameFromSessionID(sessionID), -1)
   # logout script has been got from https://stackoverflow.com/questions/179355/clearing-all-cookies-with-javascript
   print("""<script>
               var cookies = document.cookie.split("; ");
               for (var c = 0; c < cookies.length; c++) {
                     var d = window.location.hostname.split(".");
                     while (d.length > 0) {
                        var cookieBase = encodeURIComponent(cookies[c].split(";")[0].split("=")[0]) + '=; expires=Thu, 01-Jan-1970 00:00:01 GMT; domain=' + d.join('.') + ' ;path=';
                        var p = location.pathname.split('/');
                        document.cookie = cookieBase + '/';
                        while (p.length > 0) {
                           document.cookie = cookieBase + p.join('/');
                           p.pop();
                        };
                        d.shift();
                     }
               }
               window.location='index.py'
         </script>
         """)
   htmlMethods.endBodyAndHtml()
elif 'login' in form and 'username' in form.keys() and 'pwd' in form.keys():
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
      isLoginNotSuccessful = Database().updateSessionID(form["username"].value, sessionID)
      if isLoginNotSuccessful:
         htmlMethods.printHeader("Login Failed!")
         print("<p>Login Failed!</p>")
         print("<p>Something went wrong</p>")
         print("""<input type="submit" value="Go back" onclick="window.location='login.py';"/>""")
         htmlMethods.endBodyAndHtml()
      else:
         cookie["session"] = sessionID
         cookie["session"]["domain"] = "localhost"
         session_cookie = cookie.output().replace("Set-Cookie: ", "")
         htmlMethods.printHeader("Login Successful!")
         print ("<script>")
         print ("document.cookie = '%s';" % session_cookie)
         print ("window.location = 'index.py';")
         print ("</script>")
         htmlMethods.endBodyAndHtml()
else:
   htmlMethods.printHeader("Login")
   print("""<p>Login to system</p>
        <form method='POST' action='login.py'>
            <label for="username">Username:</label>
            <input type='text' name='username' required/><br><br>
            <label for="pwd">Password:</label>
            <input type='password' name='pwd' required/><br><br>
            <input type='submit' value='Login' name='login' />
        </form>
        <input type="submit" value="I don't have an account" onclick="window.location='register.py';"/><br><br>
        <input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")
   htmlMethods.endBodyAndHtml()         

