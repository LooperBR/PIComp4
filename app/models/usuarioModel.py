import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "biblioteca"
)
class UsuarioModel:
    def teste():
        print(mydb)
    
    def create(parametros,bibliotecario):
        mycursor = mydb.cursor()
        sql = "INSERT INTO usuario(login,senha,nome,cpf,bairro,rua,numero,cidade,estado,data_nascimento,bibliotecario) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (parametros["login"],parametros["senha"],parametros["nome"],parametros["cpf"],parametros["bairro"],parametros["rua"],\
            parametros["numero"],parametros["cidade"],parametros["estado"],parametros["data_nascimento"],bibliotecario)
        mycursor.execute(sql,val)
        mydb.commit()
        return mycursor.rowcount,mycursor.lastrowid
    
    def update(parametros,bibliotecario):
        mycursor = mydb.cursor()
        sql = "UPDATE usuario SET login = %s, senha = %s, nome = %s, cpf = %s, bairro = %s, rua = %s,\
             numero = %s, cidade = %s, estado = %s, data_nascimento = %s, bibliotecario = %s WHERE id = %s;"
        val = (parametros["login"],parametros["senha"],parametros["nome"],parametros["cpf"],parametros["bairro"],parametros["rua"],parametros["numero"],parametros["cidade"],parametros["estado"],parametros["data_nascimento"],bibliotecario,parametros["id"])
        mycursor.execute(sql,val)
        mydb.commit()
        return mycursor.rowcount,mycursor.lastrowid

    def getAll():
        mycursor = mydb.cursor()
        sql = "SELECT * FROM usuario;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    
    def get(id):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM usuario where id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        return myresult

# Printing the connection object
