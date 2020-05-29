#!C:\Program Files\Python36\python.exe

import os
import cgi
import random
from htmlMethods import *
from database import *

form = cgi.FieldStorage()
companyUsername = form["company"].value
allList = Database().printCompany(companyUsername)
detailsList = allList[0]
htmlMethods.printHeader("PreviousPositions")
htmlMethods.printTableHeader()

checkFlag = 0
print("""
<body>

<h2>{}:</h2>

<table style='width:100%'>
  <tr>
    <th>Name:</th>
    <td>{}</td>
  </tr>
  <tr>
    <th>Email Address:</th>
    <td>{}</td>
  </tr>
  <tr>
    <th>Telephone number:</th>
    <td>{}</td>
  </tr>
  <tr>
    <th>Website:</th>
    <td>{}</td>
  </tr>
  <tr>
    <th>City:</th>
    <td>{}</td>
  </tr>
  <tr>
    <th>Postal Address:</th>
    <td>{}</td>
  </tr>
</table>
</body>""".format(detailsList[0],detailsList[0],detailsList[1], detailsList[2], detailsList[3], detailsList[4], detailsList[5]))
            
print("""
    <input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")

htmlMethods.endBodyAndHtml()

