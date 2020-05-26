#!C:\Program Files\Python36\python.exe
import os
import cgi
from htmlMethods import htmlMethods

if "HTTP_COOKIE" in os.environ:
    htmlMethods.printHeader("index!")
    htmlMethods.endBodyAndHtml()
else:
    htmlMethods.redirect("login.html")