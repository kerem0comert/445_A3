#!C:\Program Files\Python36\python.exe
import os
import cgi
import random
from htmlMethods import *
from database import *

form = cgi.FieldStorage()

if "search" in form.keys():
    htmlMethods.printHeader("Search Result")
else:
    htmlMethods.printHeader("Active Positions")

print("""<form method='GET' action='listActivePositions.py'>
            <label for="username">Keyword for search:</label>
            <input type='text' name='search' required/><br><br>
            <input type='submit' value='Search' name='do_search' />
        </form>""")

print("""<input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")            

if "search" in form.keys():
    print("""<input type="submit" value="Clear Search Results" onclick="window.location='listActivePositions.py';"/>""")
    print("""<p>Search results for {}</p>""".format(form["search"].value))

cityCount = Database().findCityCount()
cityList = Database().getCities()
if "search" in form.keys():
    positionList = Database().searchKeywordInternshipPositions(form["search"].value)
else:
    positionList = Database().ListInternshipPositionsBycity()

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
        <th>Software Company</th>
        <th>Position Name</th>
        <th>Description</th>
        <th>Expectations</th>
        <th>Deadline</th>
    </tr>""" % cityName)

    for position in positionList:
        if(position[6] == cityName):
            print("""<tr>""")
            print('<td><a href="companydetails.py?company='+position[0]+'">'+position[1]+'</a></td>')
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

