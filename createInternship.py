#!C:\Program Files\Python36\python.exe
import os
import cgi

from htmlMethods import htmlMethods
from database import *
import http.cookies as Cookie  

form = cgi.FieldStorage()

if not form or not 'register' in form:
    htmlMethods.printHeader("Register")
    print("""<h1>Create a new Internship Position</h1>
        <form method='POST' action='register.py'>
            <label for="positionName">Position Name:</label>
            <input type='text' name='positionName' required/><br><br>
            <label for="positionDesc">Position Description:</label>
            <input type='text' name='positionDesc' required/><br><br>
            <label for="expectations">Expectations:</label>
            <input type='text' name='expections' required/><br><br>
            <label for="deadlineToApply">Email:</label>
            <input type='deadlineToApply' name='email' required/><br><br>     
        </form>
        <input type="submit" value="Create Internship" name = "createInternship" 
        onclick="window.location='login.py';"/><br><br>
        <input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")
        
    htmlMethods.endBodyAndHtml()
else:
    if "HTTP_COOKIE" in os.environ and "createInternship" in form:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        sessionID = cookie["session"].value
        username = Database().getUsernameFromSessionID(sessionID)
        elementList = ["name", "details", "expectations", "deadline"]
        formList =[]
        for elementName in elementList:
            formList.append(form[elementName].value)
        formList.append(username)
        isNotSuccessful = Database().postNewInternship(formList)

        if isNotSuccessful:
            htmlMethods.printHeader("Register Failed!")
            print("<h1>Register Failed!</h1>")
            print("<h1>Something went wrong</h1>")
            print("""<input type="submit" value="Go back" onclick="window.location='register.py';"/>""")
            htmlMethods.endBodyAndHtml()
        else:
            htmlMethods.printHeader("Register Successful!")
            print("<h1>You have registered successfully!</h1>")
            print("<h1>What do you want now?</h1>")
            print("""<input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")
            print("""<input type="submit" value="Login" onclick="window.location='login.py';"/>""")
            htmlMethods.endBodyAndHtml()
