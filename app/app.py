from flask import Flask
from flask import url_for, redirect, render_template, request
from flask import session
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'controllers')
sys.path.insert(2, 'models')

from loginController import LoginController
from usuarioController import UsuarioController


app = Flask(__name__)
app.secret_key = b'271e52fe075c9621eb86a26cce283dee515b6c870bb6afbafad6e853b0f23a99'

@app.route("/")
def index():
    return "<p>index page!</p>"

@app.route("/home")
def home():
    return "<p>home " + session["username"] + " page!</p>"

@app.get("/usuario/<usuario>")
def usuario_get(usuario):
    return UsuarioController.get(usuario)

@app.get("/login")
def login_get():

    html = render_template('header.html',name='login')
    html +=render_template('login.html',url = url_for('login_post'))
    html +=render_template('footer.html')
    return html

@app.post("/login")
def login_post():
    logou,usuario_logado=LoginController.login(request.form['login'],request.form['senha'])
    print(logou)
    if logou:
        session["username"] = usuario_logado
        return redirect('/home')
    return redirect('/login')

@app.get("/usuario")
def usuario():
    return UsuarioController.index()

@app.post("/criar_usuario")
def novo_usuario():
    UsuarioController.create(request.form)
    return redirect('/usuario')

@app.get("/easter_egg")
def easter_egg():
    return render_template('header.html',name='easter_egg')+render_template('easter_egg.html')+render_template('footer.html',scripts=[url_for('static',filename='konami.js')])

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route("/teste")
def teste():
    return "<p>Hello, "+session["username"]+"!</p>"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('usuario_get', usuario = 1))
    print(url_for('easter_egg'))