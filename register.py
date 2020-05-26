#!C:\Program Files\Python36\python.exe
import os
import cgi
from htmlMethods import htmlMethods

form = cgi.FieldStorage()

if not form or not 'register' in form:
    htmlMethods.printHeader("Register")
    print("""<p>Enter username and password: </p>
        <form method='POST' action='register.py'>
        <label for="username">Username:</label>
        <input type='text' name='username' required/><br><br>
        <label for="pwd">Password:</label>
        <input type='password' name='pwd' required/><br><br>
        <label for="companyName">Company Name:</label>
        <input type='text' name='companyName' required/><br><br>
        <label for="email">Email:</label>
        <input type='email' name='email' required/><br><br>
        <label for="telephone">Telephone:</label>
        <input type='tel' name='telephone' required/><br><br>
        <label for="website">Website:</label>
        <input type='text' name='website' required/><br><br> 
        <label for="city">City:</label>
        <input type='text' name='city' required/><br><br> 
        <label for="postalAddress">Postal Address:</label>
        <input type='text' name='postalAddress' required/><br><br> 
        <input type='submit' value='Register' name='register' />
        </form>
        <input type="submit" value="Already have an account?" onclick="window.location='login.py';"/>""")
    htmlMethods.endBodyAndHtml()
else:
    htmlMethods.printHeader("Register")
    htmlMethods.endBodyAndHtml()