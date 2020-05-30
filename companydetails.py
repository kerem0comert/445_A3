#!C:\Program Files\Python36\python.exe

import os
import cgi
import random
from htmlMethods import *
from database import *

companies = Database().getCompanies()

htmlMethods.printHeader("Company Details")
form = cgi.FieldStorage()

if "company" in form.keys():
  companyUsername = form["company"].value
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
  print ("""<h1>Select the company name you want to search:<br /></h1> 
    <form method = "get" action = "companydetails.py"> 
      <h1> 
      <select name="company" id="company">""")
  for company in companies:
    print("""<option value="{}">{}</option>""".format(company[0], company[3]))
  print("""
            </select><br><br>
      <input type = "submit" value = "Get Company Details" />
      </h1> 
    </form>""")

          
print("""<input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")

htmlMethods.endBodyAndHtml()

