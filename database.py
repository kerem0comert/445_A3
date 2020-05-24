import sqlite3
import os

dbFileName = "assignment3.db"

class Database():
    def __init__(self):
        self.db = sqlite3.connect(dbFileName, check_same_thread=False)

    def login(self, username, password):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT * FROM SOFTWARECOMPANY WHERE username = ? AND password = ?", (username,password,))
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult

    def register(self, insertDetails): # Burda bir yanlis yapmisim address yerinde city olmasi lazim duzelticem JOIN YAPILMALI****************************
        # insertDetails -> (username,password,website,name,email,telephone,address,sessionId)
        try:
            self.db.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId) 
                            VALUES (CURRENT_DATE, ?, ?, ?, ?, ?, ?, ?, ?);''', (insertDetails[0],insertDetails[1],insertDetails[2],insertDetails[3],insertDetails[4],insertDetails[5],insertDetails[6],insertDetails[7],))
            self.db.commit()
            return 0
        except: return 1 #Each company should have a unique name
    
    def postNewInternship(self, insertDetails):
        # insertDetails -> (id,name,details,name,expectations,deadline) 
        try:
            self.db.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,name,expectations,deadline) 
                            VALUES (CURRENT_DATE, ?, ?, ?, ?, ?, ?);''', (insertDetails[0],insertDetails[1],insertDetails[2],insertDetails[3],insertDetails[4],insertDetails[5],))
            self.db.commit()
            return 0
        except: return 1 

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
        dbCursor.execute("SELECT name,details,expectations,deadline FROM INTERNSHIPPOSITION WHERE  details = ? OR expectations = ? OR name = ? ORDER BY deadline DESC",(keyword),)
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult
    
    def printCompany(self,companyName):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT i.name,i.email,i.telephone,i.website,c.cityName,i.address FROM INTERNSHIPPOSITION i,CITY c WHERE c.cityCode = i.cityNo, name = ?",(companyName),)
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult


    

    