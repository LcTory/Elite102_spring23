# main file
# author: Leone

'''
By End of Week 1 (April 6)
    - Students have successfully created a github project,
    - got their coding environment set up (VSCode + MySQL)
    - created a basic welcome message and menu for their app.
'''

import mysql.connector

connection = mysql.connector.connect(user='Elite101', database='example_2', password="pass123")


cursor = connection.cursor()
testQuerry = ("select * from student")
cursor.execute(testQuerry)

for item in cursor:
    print(item)

cursor.close()
connection.close()