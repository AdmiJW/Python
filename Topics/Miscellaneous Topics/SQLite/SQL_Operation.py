import sqlite3
import requests

#   This sample program shows how to construct a database using SQLite

#   Obtain the text file which we will construct a database from
#   In this program, we are going to get the frequency that a organization had send the email. This is obtained by
#   the row 'From: <email here>', and the organization is the part after the @ in the email.
#   Eg: abc@zech.edu.co, then zech.edu.co is what we're looking for
file = requests.get('https://www.py4e.com/code3/mbox.txt').text.split('\n')

#   First, use the sqlite3.connect() method and put in the name of the database we would want to operate on.
#   If the file is non existent, it will go ahead and create one
connect = sqlite3.connect('Resources/countOrg.sqlite')
#   Obtain the cursor from the database. This cursor is how we are going to execute SQL commands
cursor = connect.cursor()

#   If the database already have the table 'Counts', then delete it. We are going to create a new one each time program is run
cursor.execute('''DROP TABLE IF EXISTS Counts''')

#   Create a table 'Counts'
cursor.execute('''CREATE TABLE "Counts" (
    'ID' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    'org' TEXT UNIQUE NOT NULL,
    'count' INTEGER NOT NULL
    );
''')

for line in file:
    #   Not the row we are looking for. Continue to next row
    if not line.startswith('From: '):
        continue

    #   Obtain the organization
    email = line.split()[1]
    org = email[ email.find('@') + 1: ]

    #   We are going to check if such organization had been recorded before in the database
    #   Notice that we are using question mark ? as placeholder, where we put a TUPLE later as arguments.
    #   We shall not directly put the information we parsed into the command itself. Hackers may put in SQL Code
    #   In execute method, we can pass in a tuple to replace the question mark in the command itself. This is one
    #   way to prevent SQL Injection (Where user maliciously put in SQL code into input fields.
    cursor.execute('SELECT org FROM Counts WHERE org= ? ', (org,) )
    isFound = cursor.fetchone()

    #   If there is NO previous record with organization, then insert it as new row
    if isFound is None:
        cursor.execute('INSERT INTO Counts (org, count) VALUES (?, 1) ', (org,) )
    #   Else we'll use UPDATE to update the value. Note we shall use the SQL Command instead of computing ourselves,
    #   This will ensure the operation is atomic, which is multi-thread safe
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ? ', (org,) )

#   sqlite3.commit() is a method which writes the data so far into the permanent storage. This may be time costly
#   so manage the frequency this method is called wisely
connect.commit()

#   Obtain the final results, which is TOP 10 most frequent organization sent email
cursor.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10')
rank = cursor.fetchall()

for individual in rank:
    print(individual)

cursor.close()
connect.close()
