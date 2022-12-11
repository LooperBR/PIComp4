import mysql.connector
 
# Creating connection object
host = "localhost"
user = "root"
password = ""
database = "biblioteca"
class LoginModel:
    
    def getUsuarioByLogin(login,senha):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT * FROM usuario WHERE login = %s and senha = %s"
        val = (login,senha)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult

# Printing the connection object
