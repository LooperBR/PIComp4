import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "biblioteca"
)
class LoginModel:
    def teste():
        print(mydb)
    
    def getUsuarioByLogin(login,senha):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM usuario WHERE login = %s and senha = %s"
        val = (login,senha)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        return myresult

# Printing the connection object
