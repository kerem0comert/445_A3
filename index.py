#!C:\Program Files\Python36\python.exe
import os
import cgi
from htmlMethods import htmlMethods

htmlMethods.printHeader("North Cyprus SW Interns")
print("""<p>Welcome to Kalkanli Internship System!</p>""")

if "HTTP_COOKIE" in os.environ:

   print("""<input type="submit" value="Log Out" onclick="window.alert("Not implemented yet!");"/>
             <input type="submit" value="Create a new Internship" onclick="window.location='createInternship.py';"/> """)
   print("""<input type="submit" value="List Previously Posted Internship Positions " onclick="window.location='listPreviousPositionsCompany.py';"/>""")
   print("""<input type="submit" value="Search An Internship Position Containing Keyword" onclick="window.location='searchKeywordMain.py';"/>""")
   print("""<input type="submit" value="List All Active Internship Positions" onclick="window.location='listActivePositions.py';"/>""")
   
else:
    print("""<input type="submit" value="Log In" onclick="window.location='login.py';"/>""")
    print("""<input type="submit" value="Register" onclick="window.location='register.py';"/>""")
    print("""<input type="submit" value="Search An Internship Position Containing Keyword" onclick="window.location='searchKeywordMain.py';"/>""")
    print("""<input type="submit" value="List All Active Internship Positions" onclick="window.location='listActivePositions.py';"/>""")
    
    

htmlMethods.endBodyAndHtml()