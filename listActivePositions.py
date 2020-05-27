#!C:\Program Files\Python36\python.exe
import os
import cgi
import random
from htmlMethods import *
from database import *

form = cgi.FieldStorage()

htmlMethods.printHeader("PreviousPositions")
cityCount = Database().findCityCount()
cityList = Database().getCities()
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
        if(position[5] == cityName):
            print("""<tr>""")
            print("""<td>%s</td>""" % position[0])
            print("""<td>%s</td>""" % position[1])
            print("""<td>%s</td>""" % position[2])
            print("""<td>%s</td>""" % position[3])
            print("""<td>%s</td>""" % position[4])
            print("""<tr>""")
            checkFlag = 1
    if not checkFlag:
        print("""<tr>""")
        print("""<td>No Position Available</td>""" )
        print("""<td> </td>""" )
        print("""<td> </td>""" )
        print("""<td> </td>""" )
        print("""<td> </td>""" )
        print("""<tr>""")
    print("""
    </table>

    </body>""")
            
print("""
    <input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")

htmlMethods.endBodyAndHtml()

