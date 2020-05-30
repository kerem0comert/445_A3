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
                      (username TEXT PRIMARY KEY,
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
					   deadline DATE NOT NULL,
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

connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp1','1234', 'google.com', 'WaffleWorld', 'testmail@gmail.com', '5556667778', 'haha street',1,1);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp2','5234', 'facebook.com', 'Moonbucks', 'testmail@gmail.com', '5556667778', 'goktasi street',1,1);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp3','2123', 'twitter.com', 'GirneBeton', 'testmail@gmail.com', '5556667778', 'aa street',1,2);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp4','2645', 'wikipedia.com', 'GirneGaz', 'testmail@gmail.com', '5556667778', 'istiklal caddesi',1,2);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp5','3489', 'foggle.com', 'DonanimHaber', 'testmail@gmail.com', '5556667778', 'aksama dogru',1,3);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp6','3488', 'toggle.com', 'TeknoSA', 'testmail@gmail.com', '5556667778', 'azalinca yagmur',1,3);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp7','9077', 'metu.com', 'Iskele1', 'testmail@gmail.com', '5556667778', 'kiz kulesi',1,4);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp8','4532', 'hetu.com', 'Iskele2', 'testmail@gmail.com', '5556667778', 've adalar',1,4);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp9','4850', 'linkedin.com', 'LefkeGaz', 'testmail@gmail.com', '5556667778', 'haha street',1,5);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp10','3321', 'mynet.com', 'LefkeBoru', 'testmail@gmail.com', '5556667778', 'haha street',1,5);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp11','3344', 'wwwa.com', 'SpaceX', 'testmail@gmail.com', '5556667778', 'haha street',1,6);''')
connection.execute('''INSERT INTO SOFTWARECOMPANY (username,password,website,name,email,telephone,address,sessionId,cityNo) VALUES ('comp12','3355', 'wwe.com', 'NASA', 'testmail@gmail.com', '5556667778', 'haha street',1,6);''')

connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (1, 'Testing Engineer', 'nodetail', 'can test stuff', date('now', '-1 days'), 'comp1');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (2, 'Software Intern', 'very detailed', 'graudate', date('now'),  'comp1');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (3, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'),  'comp1');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (4, 'Astronaut', 'nodetail', 'Should be cool', date('now', '-1 days'), 'comp2');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (5, 'Present President', 'aaa', 'graudate', date('now'), 'comp2');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (6, 'KungFu Fighter', 'nodetail', 'good loking', date('now', '+2 days'), 'comp2');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (7, 'Football Player', 'nodetail', 'messi', date('now', '-1 days'), 'comp3');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (8, 'Tennis Player', 'very detailed', 'graudate', date('now'), 'comp3');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (9, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'), 'comp3');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (10, 'Testing Engineer', 'nodetail', 'can test stuff', date('now', '-1 days'), 'comp4');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (11, 'Software Intern', 'very detailed', 'graudate', date('now'), 'comp4');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (12, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'), 'comp4');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (13, 'Testing Engineer', 'nodetail', 'can test stuff', date('now', '-1 days'), 'comp5');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (14, 'Software Intern', 'very detailed', 'graudate', date('now'), 'comp5');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (15, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'), 'comp5');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (16, 'Testing Engineer', 'nodetail', 'can test stuff', date('now', '-1 days'), 'comp6');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (17, 'Software Intern', 'very detailed', 'graudate', date('now'), 'comp6');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (18, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'), 'comp6');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (19, 'Testing Engineer', 'nodetail', 'can test stuff', date('now', '-1 days'), 'comp7');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (20, 'Software Intern', 'very detailed', 'graudate', date('now'), 'comp7');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (21, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'), 'comp7');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (22, 'Testing Engineer', 'nodetail', 'can test stuff', date('now', '-1 days'), 'comp8');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (23, 'Software Intern', 'very detailed', 'graudate', date('now'), 'comp8');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (24, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'), 'comp8');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (25, 'Testing Engineer', 'nodetail', 'can test stuff', date('now', '-1 days'), 'comp9');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (26, 'Software Intern', 'very detailed', 'graudate', date('now'), 'comp9');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (27, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'), 'comp9');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (28, 'Testing Engineer', 'nodetail', 'can test stuff', date('now', '-1 days'), 'comp10');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (29, 'Software Intern', 'very detailed', 'graudate', date('now'), 'comp10');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (30, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'), 'comp10');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (31, 'Testing Engineer', 'nodetail', 'can test stuff', date('now', '-1 days'), 'comp11');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (32, 'Software Intern', 'very detailed', 'graudate', date('now'), 'comp11');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (33, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'), 'comp11');''')


connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (34, 'Testing Engineer', 'nodetail', 'can test stuff', date('now', '-1 days'), 'comp12');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (35, 'Software Intern', 'very detailed', 'graudate', date('now'), 'comp12');''')
connection.execute('''INSERT INTO INTERNSHIPPOSITION (id,name,details,expectations,deadline,companyUsername) VALUES (36, 'Bell Boy', 'nodetail', 'good loking', date('now', '+1 days'), 'comp12');''')


connection.commit()
connection.close()
