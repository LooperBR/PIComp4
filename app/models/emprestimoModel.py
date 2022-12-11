import mysql.connector
 
# Creating connection object
host = "localhost"
user = "root"
password = ""
database = "biblioteca"

class EmprestimoModel:
    
    def create(parametros,parametros2):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "INSERT INTO emprestimo(devolvido,data_emprestimo,data_devolucao,data_estimada_devolucao,usuario_bibliotecario_id,usuario_cliente_id,livro_id)\
                VALUES(%s,%s,%s,%s,%s,%s,%s);"
        val = (parametros2["devolvido"],parametros2["data_emprestimo"],parametros2["data_devolucao"],parametros2["data_estimada_devolucao"],parametros["bibliotecario"],parametros["cliente"],parametros["livro"])
        mycursor.execute(sql,val)
        mydb.commit()
        linhas = mycursor.rowcount
        idlinha = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return linhas,idlinha
    
    def update(parametros,parametros2):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "UPDATE emprestimo SET devolvido = %s,data_emprestimo=%s,data_devolucao=%s,data_estimada_devolucao=%s,usuario_bibliotecario_id=%s,usuario_cliente_id=%s,livro_id=%s \
                WHERE id = %s;"
        val = (parametros2["devolvido"],parametros2["data_emprestimo"],parametros2["data_devolucao"],parametros2["data_estimada_devolucao"],parametros["bibliotecario"],parametros["cliente"],parametros["livro"],parametros["id"])
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
        sql = "SELECT * FROM emprestimo;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
    
    def get(id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT * FROM emprestimo where id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
    
    def getVerbose(id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT e.id,e.devolvido,e.data_emprestimo,e.data_devolucao,e.data_estimada_devolucao,ub.nome bibliotecario,uc.nome cliente,l.nome livro FROM emprestimo e \
            INNER JOIN usuario ub ON ub.id = e.usuario_bibliotecario_id \
            INNER JOIN usuario uc ON uc.id = e.usuario_cliente_id \
            INNER JOIN livro l ON l.id = e.livro_id\
            WHERE uc.id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
    
    def getAllVerbose():
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT e.id,e.devolvido,e.data_emprestimo,e.data_devolucao,e.data_estimada_devolucao,ub.nome bibliotecario,uc.nome cliente,l.nome livro FROM emprestimo e \
            INNER JOIN usuario ub ON ub.id = e.usuario_bibliotecario_id \
            INNER JOIN usuario uc ON uc.id = e.usuario_cliente_id \
            INNER JOIN livro l ON l.id = e.livro_id;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult

    def delete_livro_has_emprestimo(livro_id,emprestimo_id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "DELETE FROM livro_has_emprestimo WHERE livro_id = %s AND emprestimo_id = %s;"
        val = (livro_id,emprestimo_id)
        mycursor.execute(sql,val)
        mydb.commit()
        linhas = mycursor.rowcount
        idlinha = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return linhas,idlinha
    
    def create_livro_has_emprestimo(livro_id,emprestimo_id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "INSERT INTO livro_has_emprestimo(livro_id,emprestimo_id) \
	            VALUES(%s,%s);"
        val = (livro_id,emprestimo_id)
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
        sql = "SELECT emprestimo_id FROM livro_has_emprestimo WHERE livro_id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult