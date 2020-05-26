import sqlite3
import os

# Check if there is a db file already exists
if os.path.exists("assignment3.db"):
    print("Remove assignment3.db before creating a new one!")
    quit()

# Create the DB file
connection = sqlite3.connect('assignment3.db')

# Enable foreign keys
connection.execute('PRAGMA foreign_keys = 1')

# Create tables
connection.execute('''CREATE TABLE CITY
                      (cityCode INT PRIMARY KEY,
                       cityName TEXT NOT NULL
                      );''')
connection.execute('''CREATE TABLE SOFTWARECOMPANY
                      (username INT PRIMARY KEY,
                       password TEXT NOT NULL,
					   website TEXT NOT NULL,
					   name TEXT NOT NULL,
					   email TEXT NOT NULL,
					   telephone TEXT NOT NULL,
					   address TEXT NOT NULL,
					   sessionId INT NOT NULL,
                       cityNo INT NOT NULL,
                       FOREIGN KEY (cityNo) REFERENCES CITY(cityCode) ON UPDATE CASCADE
                      );''')
connection.execute('''CREATE TABLE INTERNSHIPPOSITION
                      (id INT PRIMARY KEY,
                       name TEXT NOT NULL,
                       details TEXT NOT NULL,
                       expectations TEXT,
					   deadline TEXT NOT NULL,
                       companyUsername TEXT NOT NULL,
                       FOREIGN KEY (companyUsername) REFERENCES SOFTWARECOMPANY(username) ON UPDATE CASCADE
                      );''')

# Insert the values to tables
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (1, 'Gazimagusa');''')
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (2, 'Girne');''')
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (3, 'Guzelyurt');''')
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (4, 'Iskele');''')
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (5, 'Lefke');''')
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (6, 'Lefkosa');''')
connection.commit()
connection.close()