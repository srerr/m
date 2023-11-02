# Program to display the data 
import mysql.connector 

mydb = mysql.connector.connect( 
host = "localhost", 
user = "root", 
password = "sreeram@521", 
database = "sreeram"
) 

mycursor = mydb.cursor() 

mycursor.execute("SELECT * FROM auth_user") 

# This SQL statement selects all data from the CUSTOMER table. 
result = mycursor.fetchall() 

# Printing all records or rows from the table. 
# It returns a result set. 
for all in result: 
    print(all)
