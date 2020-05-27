#!C:\Program Files\Python36\python.exe
import os
import cgi
import random
from htmlMethods import *
from database import *

form = cgi.FieldStorage()

htmlMethods.printHeader("PreviousPositions")
positionList = Database().ListInternshipPositions()
print("""<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>Previously Posted Internship Positions</h2>

<table>
  <tr>
    <th>Position Name</th>
    <th>Description</th>
    <th>Expectations</th>
    <th>Deadline</th>
  </tr>""")

for position in positionList:
    print("""<tr>""")
    print("""<td>%s</td>""" % position[0])
    print("""<td>%s</td>""" % position[1])
    print("""<td>%s</td>""" % position[2])
    print("""<td>%s</td>""" % position[3])
    print("""<tr>""")

print("""
</table>

</body>""")
            
print("""
    <input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")

htmlMethods.endBodyAndHtml()

