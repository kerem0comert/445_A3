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
        dbCursor.execute("SELECT username FROM SOFTWARECOMPANY WHERE sessionID = ?", (incomingSessionId))
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        try:
            queryTuple = queryResult[0]
            return queryTuple[0]
        except: return None

    def postNewInternship(self, insertDetails):
        # insertDetails -> (id,name,details,name,expectations,deadline) 
        try:
            dbCursor = self.db.cursor()
            dbCursor.execute("SELECT MAX(id) FROM INTERNSHIPPPOSITION")
            queryResult = dbCursor.fetchall()
            dbCursor.close()
            try:
                queryTuple = queryResult[0]
                maxID = queryTuple[0]
            except: maxID = 0 #the table was empty
            
            newID = maxID + 1

            self.db.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) 
                            VALUES (CURRENT_DATE, ?, ?, ?, ?, ?, ?);''', (insertDetails[0],insertDetails[1],insertDetails[2],insertDetails[3],insertDetails[4],insertDetails[5],))
            self.db.commit()
            return 0
        except: 
            return 1

    def ListInternshipPositions(self): # NEED TO SPLIT THIS INTO SEPERATE QUERIES FOR EACH CITIES*****************************
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT name,details,expectations,deadline FROM INTERNSHIPPOSITION ORDER BY deadline DESC")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult

    def ListActiveInternshipPositions(self, todayDate): # NEED TO SPLIT THIS INTO SEPERATE QUERIES FOR EACH CITIES*****************************
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT name,details,expectations,deadline FROM INTERNSHIPPOSITION WHERE deadline <= ? ORDER BY deadline DESC",(todayDate),)
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult
    
    def searchKeywordInternshipPositions(self, keyword): #Test icin ? yerine test position yazdim normalde keyword aramali
        dbCursor = self.db.cursor()
        dbCursor.execute("""SELECT s.username, s.name, i.name, i.details, i.expectations, i.deadline, c.cityName FROM INTERNSHIPPOSITION i, SOFTWARECOMPANY s, CITY c WHERE i.companyUsername=s.username AND c.cityCode=s.CityNo AND (i.details LIKE '%%an%%' OR i.expectations LIKE '%%an%%' OR i.name LIKE '%%an%%') ORDER BY deadline DESC""")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult
    

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
    
    def findCityCount(self): # NEED TO SPLIT THIS INTO SEPERATE QUERIES FOR EACH CITIES*****************************
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT COUNT ( DISTINCT cityCode ), cityName FROM CITY")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        try:
            queryTuple = queryResult[0]
            return queryTuple[0]
        except: return 0

    def findInternshipCity(self): # NEED TO SPLIT THIS INTO SEPERATE QUERIES FOR EACH CITIES*****************************
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT DISTINCT c.cityName FROM INTERNSHIPPOSITION i, SOFTWARECOMPANY s, CITY c WHERE i.companyUsername=s.username AND c.cityCode=s.CityNo")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult

    def ListInternshipPositionsBycity(self): # NEED TO SPLIT THIS INTO SEPERATE QUERIES FOR EACH CITIES*****************************
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT s.username, s.name, i.name, i.details, i.expectations, i.deadline, c.cityName FROM INTERNSHIPPOSITION i, SOFTWARECOMPANY s, CITY c WHERE i.companyUsername=s.username AND c.cityCode=s.CityNo")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult

    