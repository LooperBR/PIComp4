from livroModel import LivroModel
from autorModel import AutorModel
from flask import url_for, render_template

class LivroController:
    def create(parametros):
        print(parametros)
        return
        if(parametros["id"]=='0'):
            print("create")
            print(LivroModel.create(parametros))
        else:
            print("update")
            print(LivroModel.update(parametros))
            
        return
    
    def index():
        livros = LivroModel.getAll()
        autores = AutorModel.getAll()
        print(livros)
        html = render_template('header.html',name='Livro')
        html +=render_template('livros.html',livros = livros,autores=autores) 
        html +=render_template('footer.html',scripts=[url_for('static',filename='livros.js')])
        return html
    
    def get(id):
        livro = LivroModel.get(id)
        print(livro)
        return livro