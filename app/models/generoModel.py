import mysql.connector
 
# Creating connection object
host = "localhost"
user = "root"
password = "123456"
database = "biblioteca"

class GeneroModel:
    
    def create(parametros):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "INSERT INTO genero(nome) \
               VALUES(%s);"
        val = (parametros["nome"],)
        mycursor.execute(sql,val)
        mydb.commit()
        linhas = mycursor.rowcount
        idlinha = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return linhas,idlinha
    
    def update(parametros):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "UPDATE genero SET nome = %s WHERE id = %s;"
        val = (parametros["nome"],parametros["id"])
        mycursor.execute(sql,val)
        mydb.commit()
        linhas = mycursor.rowcount
        idlinha = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return linhas,idlinha

    def getAll():
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT * FROM genero;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
    
    def get(id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT * FROM genero where id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
