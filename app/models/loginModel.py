import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456"
)
class Login:
    def teste():
        print(mydb)
# Printing the connection object
