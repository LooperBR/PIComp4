from emprestimoModel import EmprestimoModel
from usuarioModel import UsuarioModel
from livroModel import LivroModel
from flask import url_for, render_template

class EmprestimoController:
    def create(parametros):
        print("parametros")
        print(parametros)
        parametros2 = {}

        if("devolvido" in parametros):
            parametros2["devolvido"] = 1
        else:
            parametros2["devolvido"] = 0
        
        if(parametros["data_emprestimo"]=='1970-01-01'):
            parametros2["data_emprestimo"] = None
        else:
            parametros2["data_emprestimo"] = parametros["data_emprestimo"]
        
        if(parametros["data_devolucao"]=='1970-01-01' or parametros["data_devolucao"]==''):
            parametros2["data_devolucao"] = None
        else:
            parametros2["data_devolucao"] = parametros["data_devolucao"]
        
        if(parametros["data_estimada_devolucao"]=='1970-01-01'):
            parametros2["data_estimada_devolucao"] = None
        else:
            parametros2["data_estimada_devolucao"] = parametros["data_estimada_devolucao"]
        print(parametros)
        print(parametros2)
        
        if(parametros["id"]=='0'):
            print("create")
            print(EmprestimoModel.create(parametros,parametros2))
        else:
            print("update")
            print(EmprestimoModel.update(parametros,parametros2))
            
        return
    
    def index():
        emprestimos = EmprestimoModel.getAll()
        bibliotecarios = UsuarioModel.getBibliotecarios()
        clientes = UsuarioModel.getClientes()
        livros = LivroModel.getLivrosNaoEmprestados()
        print(emprestimos)
        html = render_template('header.html',name='Emprestimo')
        html +=render_template('emprestimos.html',emprestimos = emprestimos,bibliotecarios=bibliotecarios,clientes=clientes,livros=livros)
        html +=render_template('footer.html',scripts=[url_for('static',filename='emprestimos.js')])
        return html
    
    def get(id):
        emprestimo = EmprestimoModel.get(id)
        print(emprestimo)
        return emprestimo
    
    def verEmprestimo(admin,id):
        if admin==1:
            emprestimos = EmprestimoModel.getAllVerbose()
        else:
            emprestimos = EmprestimoModel.getVerbose(id)    
        html = render_template('header.html',name='Emprestimo')
        html +=render_template('verEmprestimos.html',emprestimos = emprestimos)
        html +=render_template('footer.html')
        return html