#!C:\Program Files\Python36\python.exe
import os
import cgi
from htmlMethods import htmlMethods
from database import *
import http.cookies as Cookie  

form = cgi.FieldStorage()

if not form or not 'createInternship' in form:
    htmlMethods.printHeader("Create Internship")
    print("""<h1>Create a new Internship Position</h1>
        <form method='POST' action='createInternship.py'>
            <label for="positionName">Position Name:</label>
            <input type='text' name='positionName' required/><br><br>
            <label for="positionDesc">Position Description:</label>
            <input type='text' name='positionDesc' required/><br><br>
            <label for="expectations">Expectations:</label>
            <input type='text' name='expections' required/><br><br>
            <label for="deadline">Deadline:</label>
            <input type='date' name='deadline' required/><br><br> 
            <input type="submit" value="Create Internship" name = "createInternship"/><br><br>
        </form>
        <input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")
        
    htmlMethods.endBodyAndHtml()
else:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    sessionID = cookie["session"].value
    companyUsername = Database().getUsernameFromSessionID(sessionID)
    elementList = ["positionName", "positionDesc", "expections", "deadline"]
    formList =[]
    for elementName in elementList:
        formList.append(form[elementName].value)
    formList.append(companyUsername)
    isNotSuccessful = Database().postNewInternship(formList)

    if isNotSuccessful:
        htmlMethods.printHeader("Creation Failed!")
        print("<h1>Internship Creation Failed!</h1>")
        print("<h1>Something went wrong</h1>")
        print("""<input type="submit" value="Go back" onclick="window.location='createInternship.py';"/>""")
        htmlMethods.endBodyAndHtml()
    else:
        htmlMethods.printHeader("Creation Successful!")
        print("<h1>Internship Creation has been completed successfully!</h1>")
        print("<h1>What do you want now?</h1>")
        print("""<input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")
        print("""<input type="submit" value="Create Another Internship Position" onclick="window.location='createInternship.py';"/>""")
        htmlMethods.endBodyAndHtml()
