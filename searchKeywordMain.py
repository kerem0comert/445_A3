#!C:\Program Files\Python36\python.exe
import os
import cgi
import random
from htmlMethods import *
from database import *

form = cgi.FieldStorage()
htmlMethods.printHeader("Search ")
print("""<p>Enter a keyword to search</p>
            <form method='POST' action='searchKeywordResult.py'>
                <label for="keyword">Keyword:</label>
                <input type='text' name='keyword' required/><br><br>
            </form>
        <input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")
print("""
    <input type="submit" value="Search" onclick="window.location='searchKeywordResult.py';"/>""")
