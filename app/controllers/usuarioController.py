from usuarioModel import UsuarioModel
from flask import url_for
from flask import render_template

class UsuarioController:
    def create(parametros):
        bibliotecario = 0
        if("bibliotecario" in parametros):
            bibliotecario = 1
        
        if(parametros["id"]==0):
            print(UsuarioModel.create(parametros,bibliotecario))
        else:
            print(UsuarioModel.update(parametros,bibliotecario))
        print(parametros)
        
        return UsuarioController.index()
    
    def index():
        usuarios = UsuarioModel.getAll()
        html = render_template('header.html',name='login')
        html +=render_template('usuarios.html',url = url_for('novo_usuario'),usuarios = usuarios)
        html +=render_template('footer.html',scripts=[url_for('static',filename='usuarios.js')])
        return html
    
    def get(id):
        return UsuarioModel.get(id)