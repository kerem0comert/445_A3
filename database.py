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
        try:
            username = self.db.execute("SELECT username FROM SOFTWARECOMPANY WHERE sessionID = ?", (incomingSessionId))
            return username[0]
        except:
            return None

    def postNewInternship(self, insertDetails):
        # insertDetails -> (id,name,details,name,expectations,deadline) 
        try:
            try: 
                maxTuple = self.db.execute('SELECT MAX(id) FROM INTERNSHIPPPOSITION')
                maxID = maxTuple[0]
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
    
    def searchKeywordInternshipPositions(self, keyword): 
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT name,details,expectations,deadline FROM INTERNSHIPPOSITION WHERE  details LIKE % OR expectations LIKE % OR name LIKE % ORDER BY deadline DESC",(keyword),)
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult
    
    def printCompany(self,companyName):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT i.name,i.email,i.telephone,i.website,c.cityName,i.address FROM INTERNSHIPPOSITION i,CITY c WHERE c.cityCode = i.cityNo, name = ?",(companyName),)
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult

    def getCities(self):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT cityName FROM CITY")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult


    

    