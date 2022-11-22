from flask import Flask
from flask import url_for, redirect, render_template, request
from flask import session
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'controllers')
sys.path.insert(2, 'models')

from loginController import LoginController
from usuarioController import UsuarioController
from editoraController import EditoraController
from autorController import AutorController


app = Flask(__name__)
app.secret_key = b'271e52fe075c9621eb86a26cce283dee515b6c870bb6afbafad6e853b0f23a99'

@app.route("/")
def index():
    return redirect('/home')

@app.route("/home")
def home():

    html = render_template('header.html',name='home')
    html +=render_template('home.html')
    html +=render_template('footer.html')

    return html

@app.get("/login")
def login_get():

    if('username' in session):
        return redirect('/home')

    html = render_template('header.html',name='login')
    html +=render_template('login.html',url = url_for('login_post'))
    html +=render_template('footer.html')
    return html

@app.post("/login")
def login_post():
    logou,usuario_logado,bibliotecario=LoginController.login(request.form['login'],request.form['senha'])
    print(logou)
    if logou:
        session["username"] = usuario_logado
        session["bibliotecario"] = bibliotecario
        return redirect('/home')
    return redirect('/login')

@app.get("/usuario/<usuario>")
def usuario_get(usuario):
    if not 'username' in session:
        return 'Você precisa estar logado para acessar essa página'
    elif not session['bibliotecario']:
        return 'Seu usuário não tem permissão para ver essa página'
    
    return UsuarioController.get(usuario)

@app.get("/usuario")
def usuario():
    if not 'username' in session:
        return 'Você precisa estar logado para acessar essa página'
    elif not session['bibliotecario']:
        return 'Seu usuário não tem permissão para ver essa página'
    return UsuarioController.index()

@app.post("/criar_usuario")
def novo_usuario():
    UsuarioController.create(request.form)
    return redirect('/usuario')

@app.get("/editora/<editora>")
def editora_get(editora):
    if not 'username' in session:
        return 'Você precisa estar logado para acessar essa página'
    elif not session['bibliotecario']:
        return 'Seu usuário não tem permissão para ver essa página'
    
    return EditoraController.get(editora)

@app.get("/editora")
def editora():
    if not 'username' in session:
        return 'Você precisa estar logado para acessar essa página'
    elif not session['bibliotecario']:
        return 'Seu usuário não tem permissão para ver essa página'
    return EditoraController.index()

@app.post("/criar_editora")
def nova_editora():
    EditoraController.create(request.form)
    return redirect('/editora')

@app.get("/autor/<autor>")
def editora_get(autor):
    if not 'username' in session:
        return 'Você precisa estar logado para acessar essa página'
    elif not session['bibliotecario']:
        return 'Seu usuário não tem permissão para ver essa página'
    
    return AutorController.get(autor)

@app.get("/autor")
def editora():
    if not 'username' in session:
        return 'Você precisa estar logado para acessar essa página'
    elif not session['bibliotecario']:
        return 'Seu usuário não tem permissão para ver essa página'
    return AutorController.index()

@app.post("/criar_autor")
def novo_autor():
    AutorController.create(request.form)
    return redirect('/autor')

@app.get("/easter_egg")
def easter_egg():
    return render_template('header.html',name='easter_egg')+render_template('easter_egg.html')+render_template('footer.html',scripts=[url_for('static',filename='konami.js')])

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('bibliotecario', None)
    return redirect('/login')

@app.route("/teste")
def teste():
    return "<p>Hello, "+session["username"]+"!</p>"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('usuario_get', usuario = 1))
    print(url_for('easter_egg'))