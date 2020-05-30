#!C:\Program Files\Python36\python.exe

import os
import cgi
import random
from htmlMethods import *
from database import *
import re

htmlMethods.printHeader("Company Details")
form = cgi.FieldStorage()


if "company" in form.keys() or "companySearch" in form.keys():
  if "companySearch" in form.keys():
    companyName = form["companySearch"].value
    print("aaaaaaaaaaaaaaaaaaaaaa", companyName)
    companyUsername = Database().getUsernameFromCompanyName(companyName)[0] #this returns ['1234',] why?
    #companyRegex = "^'*'$"
    #print("match", re.match(companyRegex, companyUsername))
  else: companyUsername = form["company"].value
  companyUsername = str(companyUsername)[1:5]
  print("aaaaaaaaaaaaaaaaaaaaaa", companyUsername)
  allList = Database().printCompany(companyUsername)
  detailsList = allList[0]
  htmlMethods.printTableHeader()
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
else:
  print ("""<p>Enter the company name you want to search:<br /></p> 
    <form method = "get" action = "companydetails.py"> 
      <p> 
      <input type = "text" name = "companySearch" />
      <input type = "submit" value = "Search" />
      </p> 
    </form>""")

          
print("""<input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")

htmlMethods.endBodyAndHtml()

