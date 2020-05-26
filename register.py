#!C:\Program Files\Python36\python.exe

import os
import cgi
from printHeader import printHeader

printHeader.printHeader("KIS - Register")  

form = cgi.FieldStorage()

#database has to be checked for the uniquness of the username
if 'register' in form and and 'username' in form.keys() and 'pwd' in form.keys()