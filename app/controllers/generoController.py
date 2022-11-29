from generoModel import GeneroModel
from flask import url_for, render_template

class GeneroController:
    def create(parametros):
        print(parametros)

        if(parametros["id"]=='0'):
            print("create")
            print(GeneroModel.create(parametros))
        else:
            print("update")
            print(GeneroModel.update(parametros))
            
        return
    
    def index():
        generos = GeneroModel.getAll()
        print(generos)
        html = render_template('header.html',name='Autor')
        html +=render_template('generos.html',generos = generos)
        html +=render_template('footer.html',scripts=[url_for('static',filename='generos.js')])
        return html
    
    def get(id):
        genero = GeneroModel.get(id)
        print(genero)
        return genero