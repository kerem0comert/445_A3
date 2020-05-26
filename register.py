#!C:\Program Files\Python36\python.exe
import os
import cgi

from htmlMethods import htmlMethods
from database import *

form = cgi.FieldStorage()

if not form or not 'register' in form:
    htmlMethods.printHeader("Register")
    print("""<p>Register to system</p>
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
            <label for="cities">Select a city:</label>
            <select name="cities">
            <option value="1">Gazimagusa</option>
            <option value="2">Girne</option>
            <option value="3">Guzelyurt</option>
            <option value="4">Iskele</option>
            <option value="5">Lefke</option>
            <option value="6">Lefkosa</option>
            </select><br><br> 
            <label for="address">Address:</label>
            <input type='text' name='address' required/><br><br> 
            <input type='submit' value='Register' name='register' />
        </form>
        <input type="submit" value="Already have an account?" onclick="window.location='login.py';"/><br><br>
        <input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")
        
    htmlMethods.endBodyAndHtml()
else:
    elementList = ["username", "pwd", "companyName", "email", "telephone", "website", "cities", "address"]
    formList =[]
    for elementName in elementList:
        formList.append(form[elementName].value)
    isNotSuccessful = Database().register(formList)

    if isNotSuccessful:
        htmlMethods.printHeader("Register Failed!")
        print("<p>Register Failed!</p>")
        print("<p>Something went wrong</p>")
        print("""<input type="submit" value="Go back" onclick="window.location='register.py';"/>""")
        htmlMethods.endBodyAndHtml()
    else:
        htmlMethods.printHeader("Register Successful!")
        print("<p>You have registered successfully!</p>")
        print("<p>What do you want now?</p>")
        print("""<input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")
        print("""<input type="submit" value="Login" onclick="window.location='login.py';"/>""")
        htmlMethods.endBodyAndHtml()
