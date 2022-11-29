from autorModel import AutorModel
from flask import url_for, render_template

class AutorController:
    def create(parametros):
        print(parametros)

        if(parametros["id"]=='0'):
            print("create")
            print(AutorModel.create(parametros))
        else:
            print("update")
            print(AutorModel.update(parametros))
            
        return
    
    def index():
        autores = AutorModel.getAll()
        print(autores)
        html = render_template('header.html',name='Autor')
        html +=render_template('autores.html',autores = autores)
        html +=render_template('footer.html',scripts=[url_for('static',filename='autores.js')])
        return html
    
    def get(id):
        autor = AutorModel.get(id)
        print(autor)
        return autor