import mysql.connector
 
# Creating connection object
host = "localhost"
user = "root"
password = ""
database = "biblioteca"

class EditoraModel:
    
    def create(parametros):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "INSERT INTO editora(nome) \
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
        sql = "UPDATE editora SET nome = %s WHERE id = %s;"
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
        sql = "SELECT * FROM editora;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
    
    def get(id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT * FROM editora where id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult

    def delete_livro_has_editora(livro_id,editora_id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "DELETE FROM livro_has_editora WHERE livro_id = %s AND editora_id = %s;"
        val = (livro_id,editora_id)
        mycursor.execute(sql,val)
        mydb.commit()
        linhas = mycursor.rowcount
        idlinha = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return linhas,idlinha
    
    def create_livro_has_editora(livro_id,editora_id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "INSERT INTO livro_has_editora(livro_id,editora_id) \
	            VALUES(%s,%s);"
        val = (livro_id,editora_id)
        mycursor.execute(sql,val)
        mydb.commit()
        linhas = mycursor.rowcount
        idlinha = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return linhas,idlinha

    def getByLivroId(id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT editora_id FROM livro_has_editora WHERE livro_id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult