#!C:\Program Files\Python36\python.exe

import os
import cgi
import random
from htmlMethods import *
from database import *

form = cgi.FieldStorage()

detailsList = Database().printCompany("1234")

htmlMethods.printHeader("PreviousPositions")
htmlMethods.printTableHeader()

checkFlag = 0
print("""
<body>

<h2>%s</h2>

<table>
<tr>
    <th>Name</th>
    <th>Email Name</th>
    <th>Telephone</th>
    <th>Website</th>
    <th>City Name</th>
    <th>Address</th>
</tr>""" % "Aselsan")

for detail in detailsList:
    print("""<tr>""")
    print("""<td>%s</td>""" % detail[0])
    print("""<td>%s</td>""" % detail[1])
    print("""<td>%s</td>""" % detail[2])
    print("""<td>%s</td>""" % detail[3])
    print("""<td>%s</td>""" % detail[4])
    print("""<td>%s</td>""" % detail[5])
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

