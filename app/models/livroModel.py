import mysql.connector

from autorModel import AutorModel
from editoraModel import EditoraModel
from generoModel import GeneroModel
 
# Creating connection object
host = "localhost"
user = "root"
password = ""
database = "biblioteca"

class LivroModel:
    
    def create(parametros):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "INSERT INTO livro(nome,edicao) \
               VALUES(%s,%s);"
        val = (parametros["nome"],parametros["edicao"],)
        mycursor.execute(sql,val)
        mydb.commit()
        linhas = mycursor.rowcount
        idlinha = mycursor.lastrowid
        autores = []
        for i in parametros:
            if(i.startswith('autor')):
                autores.append(parametros[i])
        
        for i in autores:
            AutorModel.create_livro_has_autor(idlinha, i)
        print(autores)

        editoras = []
        for i in parametros:
            if(i.startswith('editora')):
                editoras.append(parametros[i])
        
        for i in editoras:
            EditoraModel.create_livro_has_editora(idlinha, i)

        generos = []
        for i in parametros:
            if(i.startswith('genero')):
                generos.append(parametros[i])
        
        for i in generos:
            GeneroModel.create_livro_has_genero(idlinha, i)

        mycursor.close()
        mydb.close()
        return linhas,idlinha
    
    def update(parametros):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "UPDATE livro SET nome = %s, edicao = %s WHERE id = %s;"
        val = (parametros["nome"],parametros["edicao"],parametros["id"])
        mycursor.execute(sql,val)
        mydb.commit()
        linhas = mycursor.rowcount
        idlinha = mycursor.lastrowid
        autores = []
        print('porra')
        for i in parametros:
            if(i.startswith('autor')):
                autores.append(int(parametros[i]))

        autoresBanco = []
        autoresBancoFudido = AutorModel.getByLivroId(parametros["id"])
        for i in autoresBancoFudido:
            autoresBanco.append(i[0])
        
        print('autoresBanco')
        print(autoresBanco)
        print('autores')
        print(autores)
        for i in autores:
            if(not i in autoresBanco):
                AutorModel.create_livro_has_autor(parametros["id"], i)
            else:
                autoresBanco.remove(i)
                

        for i in autoresBanco:
            AutorModel.delete_livro_has_autor(parametros["id"], i)
            
        editoras = []
        print('porra')
        for i in parametros:
            if(i.startswith('editora')):
                editoras.append(int(parametros[i]))

        editorasBanco = []
        editorasBancoFudido = EditoraModel.getByLivroId(parametros["id"])
        for i in editorasBancoFudido:
            editorasBanco.append(i[0])
        
        print('editorasBanco')
        print(editorasBanco)
        print('editoras')
        print(editoras)
        for i in editoras:
            if(not i in editorasBanco):
                EditoraModel.create_livro_has_editora(parametros["id"], i)
            else:
                editorasBanco.remove(i)
                

        for i in editorasBanco:
            EditoraModel.delete_livro_has_editora(parametros["id"], i)

        generos = []
        print('porra')
        for i in parametros:
            if(i.startswith('genero')):
                generos.append(int(parametros[i]))

        generosBanco = []
        generosBancoFudido = GeneroModel.getByLivroId(parametros["id"])
        for i in generosBancoFudido:
            generosBanco.append(i[0])
        
        print('generosBanco')
        print(generosBanco)
        print('generos')
        print(generos)
        for i in generos:
            if(not i in generosBanco):
                GeneroModel.create_livro_has_genero(parametros["id"], i)
            else:
                generosBanco.remove(i)
                

        for i in generosBanco:
            GeneroModel.delete_livro_has_genero(parametros["id"], i)

        mycursor.close()
        mydb.close()
        return linhas,idlinha

    def getAll():
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT * FROM livro;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult

    def getAllWithForeign():
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT l.id,l.nome,l.edicao,GROUP_CONCAT(distinct a.nome SEPARATOR ',') autores,GROUP_CONCAT(distinct e.nome SEPARATOR ',') editoras,GROUP_CONCAT(distinct g.nome SEPARATOR ',') generos FROM livro l \
LEFT JOIN livro_has_autor la ON l.id = la.livro_id \
LEFT JOIN autor a ON a.id = la.autor_id \
LEFT JOIN livro_has_editora le ON l.id = le.livro_id \
LEFT JOIN editora e ON e.id = le.editora_id \
LEFT JOIN livro_has_genero lg ON l.id = lg.livro_id \
LEFT JOIN genero g ON g.id = lg.genero_id \
GROUP BY l.id,l.nome,l.edicao;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
    
    def get(id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT * FROM livro where id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
    
    def getLivrosNaoEmprestados():
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT l.id,l.nome,EXISTS( \
                SELECT * FROM emprestimo e WHERE e.livro_id = l.id AND devolvido = 0 \
            ) emprestado FROM livro l;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
    
    def get_autores(id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT autor_id FROM livro_has_autor where livro_id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult
    
    def get_editoras(id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT editora_id FROM livro_has_editora where livro_id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult

    def get_generos(id):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT genero_id FROM livro_has_genero where livro_id = %s;"
        val = (id,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult

    def getRandom(number):
        mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
        mycursor = mydb.cursor()
        sql = "SELECT l.id,l.nome,l.edicao,GROUP_CONCAT(distinct a.nome SEPARATOR ',') autores,GROUP_CONCAT(distinct e.nome SEPARATOR ',') editoras,GROUP_CONCAT(distinct g.nome SEPARATOR ',') generos FROM livro l \
                LEFT JOIN livro_has_autor la ON l.id = la.livro_id \
                LEFT JOIN autor a ON a.id = la.autor_id \
                LEFT JOIN livro_has_editora le ON l.id = le.livro_id \
                LEFT JOIN editora e ON e.id = le.editora_id \
                LEFT JOIN livro_has_genero lg ON l.id = lg.livro_id \
                LEFT JOIN genero g ON g.id = lg.genero_id \
                WHERE NOT EXISTS(\
                    SELECT * FROM emprestimo em WHERE em.livro_id = l.id AND devolvido = 0\
                )\
                GROUP BY l.id,l.nome,l.edicao \
                ORDER BY RAND() \
                LIMIT %s;"
        val = (number,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return myresult