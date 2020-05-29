#!C:\Program Files\Python36\python.exe
import os
import cgi
from htmlMethods import htmlMethods

htmlMethods.printHeader("North Cyprus SW Interns")
print("""<p>Welcome to Kalkanli Internship System!</p>""")

if "HTTP_COOKIE" in os.environ:
    print("""<input type="submit" value="Log Out" onclick="logout();"/>""")
    print("""<input type="submit" value="Create a new Internship" onclick="window.location='createInternship.py';"/>""")
    print("""<input type="submit" value="List Previously Posted Internship Positions " onclick="window.location='listPreviousPositionsCompany.py';"/>""")
else:
    print("""<input type="submit" value="Log In" onclick="window.location='login.py';"/>""")
    print("""<input type="submit" value="Register" onclick="window.location='register.py';"/>""")

print("""<input type="submit" value="Search An Internship Position Containing Keyword" onclick="window.location='searchKeywordMain.py';"/>""")
print("""<input type="submit" value="List All Active Internship Positions" onclick="window.location='listActivePositions.py';"/>""")

print("</body>")
# logout script has been got from https://stackoverflow.com/questions/179355/clearing-all-cookies-with-javascript
print("""<script>  
    function logout() {
        var cookies = document.cookie.split("; ");
        for (var c = 0; c < cookies.length; c++) {
            var d = window.location.hostname.split(".");
            while (d.length > 0) {
                var cookieBase = encodeURIComponent(cookies[c].split(";")[0].split("=")[0]) + '=; expires=Thu, 01-Jan-1970 00:00:01 GMT; domain=' + d.join('.') + ' ;path=';
                var p = location.pathname.split('/');
                document.cookie = cookieBase + '/';
                while (p.length > 0) {
                    document.cookie = cookieBase + p.join('/');
                    p.pop();
                };
                d.shift();
            }
        }
        location.reload()
    }
</script>  
""")
print("</html>")