#!C:\Program Files\Python36\python.exe
import os
import cgi
from htmlMethods import htmlMethods

htmlMethods.printHeader("KIS Login")


form = cgi.FieldStorage()
