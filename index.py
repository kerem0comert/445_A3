import os, cgi

#!/Python36/python  
# Example using QUERY_STRING.  

def printHeader( title ):
   print ("""Content-type: text/html
    <?xml version = "1.0" encoding = "UTF-8"?
    <!DOCTYPE html PUBLIC
        "-//W3C//DTD XHTML 1.0 Strict//EN"
        "DTD/xhtml1-strict.dtd">
    <html xmlns = "http://www.w3.org/1999/xhtml">
    <head><title>%s</title></head>
    <body>""" % title) 


printHeader("QUERY_STRING example")  
print ("<h1>Name/Value Pairs</h1>")  

query = os.environ["QUERY_STRING"]    
if len(query) == 0:  
   print ("""<p><br /> 
      Please add some name-value pairs to the URL above. 
      Or try 
      <a href = "index.py?name=Veronica&age=23">this</a>. 
      </p>""")  
else:     
    print ("""<p style = "font-style: italic"> 
      The query string is '%s'.</p>""" % cgi.escape(query))  
    pairs = cgi.parse_qs(query)   
    for key, value in pairs.items():  
        print ("<p>You set '%s' to value %s</p>" % (key, value))               
print ("</body></html>")



  