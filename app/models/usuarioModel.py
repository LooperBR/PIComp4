import mysql.connector
 
# Creating connection object
host = "localhost"
user = "root"
password = "123456"
database = "biblioteca"

class UsuarioModel:
    
    def create(parametros,bibliotecario,ativo):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "INSERT INTO usuario(login,senha,nome,cpf,bairro,rua,numero,cidade,estado,data_nascimento,bibliotecario,ativo) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (parametros["login"],parametros["senha"],parametros["nome"],parametros["cpf"],parametros["bairro"],parametros["rua"],\
            parametros["numero"],parametros["cidade"],parametros["estado"],parametros["data_nascimento"],bibliotecario,ativo)
        mycursor.execute(sql,val)
        mydb.commit()
        linhas = mycursor.rowcount
        idlinha = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return linhas,idlinha
    
    def update(parametros,bibliotecario,ativo):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "UPDATE usuario SET login = %s, senha = %s, nome = %s, cpf = %s, bairro = %s, rua = %s,\
             numero = %s, cidade = %s, estado = %s, data_nascimento = %s, bibliotecario = %s, ativo = %s WHERE id = %s;"
        val = (parametros["login"],parametros["senha"],parametros["nome"],parametros["cpf"],parametros["bairro"],parametros["rua"],parametros["numero"],parametros["cidade"],parametros["estado"],parametros["data_nascimento"],bibliotecario,ativo,parametros["id"])
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
        sql = "SELECT * FROM usuario;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
    
    def get(id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT * FROM usuario where id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
