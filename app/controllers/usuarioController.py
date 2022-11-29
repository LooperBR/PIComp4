from usuarioModel import UsuarioModel
from flask import url_for, redirect, render_template

class UsuarioController:
    def create(parametros):
        bibliotecario = 0
        ativo = 0
        if("bibliotecario" in parametros):
            bibliotecario = 1
        if("ativo" in parametros):
            ativo = 1
        print(parametros)

        if(parametros["id"]=='0'):
            print("create")
            print(UsuarioModel.create(parametros,bibliotecario,ativo))
        else:
            print("update")
            print(UsuarioModel.update(parametros,bibliotecario,ativo))
            
        return
    
    def index():
        usuarios = UsuarioModel.getAll()
        html = render_template('header.html',name='login')
        html +=render_template('usuarios.html',usuarios = usuarios)
        html +=render_template('footer.html',scripts=[url_for('static',filename='usuarios.js')])
        return html
    
    def get(id):
        usuario = UsuarioModel.get(id)
        print(usuario)
        return usuario