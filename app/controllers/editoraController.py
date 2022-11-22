from editoraModel import EditoraModel
from flask import url_for, render_template

class EditoraController:
    def create(parametros):
        print(parametros)

        if(parametros["id"]=='0'):
            print("create")
            print(EditoraModel.create(parametros))
        else:
            print("update")
            print(EditoraModel.update(parametros))
            
        return
    
    def index():
        editoras = EditoraModel.getAll()
        html = render_template('header.html',name='login')
        html +=render_template('editoras.html',url = url_for('novo_usuario'),editoras = editoras)
        html +=render_template('footer.html',scripts=[url_for('static',filename='editoras.js')])
        return html
    
    def get(id):
        editora = EditoraModel.get(id)
        print(editora)
        return editora