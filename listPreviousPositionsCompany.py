#!C:\Program Files\Python36\python.exe
import os
import cgi
import random
from htmlMethods import *
from database import *
import http.cookies as Cookie

form = cgi.FieldStorage()
cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
sessionID = cookie["session"].value
companyName = Database().getCompanyNameFromSessionID(sessionID)
companyUsername = Database().getUsernameFromSessionID(sessionID)

if "search" in form.keys():
    htmlMethods.printHeader("Search Result")
else:
    htmlMethods.printHeader("Previous Positions")

print("""<form method='GET' action='listPreviousPositionsCompany.py'>
            <label for="search">Keyword for search:</label>
            <input type='text' name='search' required/><br><br>
            <input type='submit' value='Search' name='do_search' />
        </form>""")

print("""<input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")            

if "search" in form.keys():
    print("""<input type="submit" value="Clear Search Results" onclick="window.location='listPreviousPositionsCompany.py';"/>""")
    print("""<p>Search results for {}</p>""".format(form["search"].value))

print("""<p>All Internship Positions created by """ + companyName +"""</p>""")

cityCount = Database().findCityCount()
cityList = Database().getCities()
if "search" in form.keys():
    positionList = Database().ListInternshipPositionsByCity(form["search"].value, previous=True, companyUsername=companyUsername)
else:
    positionList = Database().ListInternshipPositionsByCity(previous=True, companyUsername=companyUsername)

counter = 0
htmlMethods.printTableHeader()
for city in cityList:
    checkFlag = 0
    cityName = city[1]
    print("""
    <body>

    <h2>%s</h2>

    <table>
    <tr>
        <th>Position Name</th>
        <th>Description</th>
        <th>Expectations</th>
        <th>Deadline</th>
    </tr>""" % cityName)

    for position in positionList:
        if(position[6] == cityName):
            print("""<tr>""")
            print("""<td>%s</td>""" % position[2])
            print("""<td>%s</td>""" % position[3])
            print("""<td>%s</td>""" % position[4])
            print("""<td>%s</td>""" % position[5])
            print("""<tr>""")
            checkFlag = 1
    if not checkFlag:
        print("""<tr>""")
        if "search" in form.keys():
            print("""<td>No Search Result For This City</td>""" )
        else:
            print("""<td>No Position Available</td>""" )
        print("""<td> </td>""" )
        print("""<td> </td>""" )
        print("""<td> </td>""" )
        print("""<td> </td>""" )
        print("""<tr>""")
    print("""
    </table>

    </body>""")

htmlMethods.endBodyAndHtml()

