from livroModel import LivroModel
from autorModel import AutorModel
from generoModel import GeneroModel
from editoraModel import EditoraModel
from flask import url_for, render_template

class LivroController:
    def create(parametros):
        print(parametros)
        if(parametros["id"]=='0'):
            print("create")
            print(LivroModel.create(parametros))
        else:
            print("update")
            print(LivroModel.update(parametros))
            
        return
    
    def index():
        livros = LivroModel.getAllWithForeign()
        autores = AutorModel.getAll()
        editoras = EditoraModel.getAll()
        generos = GeneroModel.getAll()
        print(livros)
        html = render_template('header.html',name='Livro')
        html +=render_template('livros.html',livros = livros,autores=autores,editoras=editoras,generos=generos) 
        html +=render_template('footer.html',scripts=[url_for('static',filename='livros.js')])
        return html
    
    def get(id):
        livro = LivroModel.get(id)
        autores = LivroModel.get_autores(id)
        editoras = LivroModel.get_editoras(id)
        generos = LivroModel.get_generos(id)
        print(livro)
        print(autores)
        livro.append(autores)
        livro.append(editoras)
        livro.append(generos)

        return livro
    
    def getRandom(number):
        livro = LivroModel.getRandom(number)
        return livro