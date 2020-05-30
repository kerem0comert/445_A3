import sqlite3
import os

dbFileName = "assignment3.db"

class Database():
    def __init__(self):
        self.db = sqlite3.connect(dbFileName, check_same_thread=False)

    def login(self, username, password):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT sessionId FROM SOFTWARECOMPANY WHERE username = ? AND password = ?", (username,password,))
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        try:
            queryTuple = queryResult[0]
            return queryTuple[0]
        except: return 0

    def register(self, insertDetails):
        # insertDetails -> [username, pwd, companyName, email, telephone, website, city, address]
        try:
            self.db.execute('''INSERT INTO SOFTWARECOMPANY (username,password,name,email,telephone,website,cityNo,address,sessionId) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', (insertDetails[0],insertDetails[1],insertDetails[2],insertDetails[3],insertDetails[4],insertDetails[5],int(insertDetails[6]), insertDetails[7], -1,))
            self.db.commit()
            return 0
        except:
            return 1
    
    def updateSessionID(self, username, sessionId):
        try:
            self.db.execute("UPDATE SOFTWARECOMPANY SET sessionId = ? WHERE username = ?", (sessionId,username,))
            self.db.commit()
            return 0
        except:
            return 1

    def getUsernameFromSessionID(self, incomingSessionId):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT username FROM SOFTWARECOMPANY WHERE sessionID = ?", (incomingSessionId,))
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        try:
            queryTuple = queryResult[0]
            return queryTuple[0]
        except: return None

    def getCompanyNameFromSessionID(self, incomingSessionId):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT name FROM SOFTWARECOMPANY WHERE sessionID = ?", (incomingSessionId,))
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        try:
            queryTuple = queryResult[0]
            return queryTuple[0]
        except: return None

    def postNewInternship(self, insertDetails):
        try:
            dbCursor = self.db.cursor()
            dbCursor.execute("SELECT MAX(id) FROM INTERNSHIPPOSITION")
            queryResult = dbCursor.fetchall()
            dbCursor.close()
            try:
                queryTuple = queryResult[0]
                maxID = queryTuple[0]
            except: maxID = 0 #the table was empty
            
            newID = maxID + 1

            self.db.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) 
                            VALUES (?, ?, ?, ?, date(?), ?);''', (newID, insertDetails[0],insertDetails[1],insertDetails[2],insertDetails[3],insertDetails[4],))
            self.db.commit()
            return 0
        except:
            return 1

    def printCompany(self,companyUsername):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT s.name,s.email,s.telephone,s.website,c.cityName,s.address FROM SOFTWARECOMPANY s,CITY c, INTERNSHIPPOSITION i WHERE c.cityCode = s.cityNo AND i.companyUsername = s.username AND i.companyUsername = ?",(companyUsername,))
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult

    def getCities(self):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT * FROM CITY")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult

    def getCompanies(self):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT * FROM SOFTWARECOMPANY")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult
    
    def findCityCount(self):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT COUNT ( DISTINCT cityCode ), cityName FROM CITY")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        try:
            queryTuple = queryResult[0]
            return queryTuple[0]
        except: return 0

    def ListInternshipPositionsByCity(self, keyword = None, previous = False, companyUsername = None):
        queryString = """SELECT s.username, s.name, i.name, i.details, i.expectations, i.deadline, c.cityName FROM INTERNSHIPPOSITION i, SOFTWARECOMPANY s, CITY c 
                            WHERE i.companyUsername=s.username AND c.cityCode=s.CityNo"""
        if not previous:
            queryString += """ AND i.deadline > datetime('now', '-1 days')"""
        if companyUsername:
            queryString += """ AND i.companyUsername='""" + companyUsername + """'"""
        if keyword:
            queryString += """ AND (c.cityName LIKE '%%{}%%' OR s.name LIKE '%%{}%%' OR i.details LIKE '%%{}%%' OR i.expectations LIKE '%%{}%%' OR i.name LIKE '%%{}%%' OR i.deadline LIKE '%%{}%%') ORDER BY deadline DESC""".format(keyword,keyword,keyword,keyword,keyword, keyword)  
        dbCursor = self.db.cursor()
        dbCursor.execute(queryString)
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult