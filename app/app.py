from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'controllers')
sys.path.insert(2, 'models')

from loginModel import Login


app = Flask(__name__)

@app.route("/")
def index():
    return "<p>index page!</p>"

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/usuario/<usuario>")
def usuario_get(usuario):
    return "<p>Ola "+usuario+"!</p>"

@app.post("/usuario/<usuario>")
def usuario_post(usuario):
    return "<p>Ola post "+usuario+"!</p>"

@app.get("/login")
def login_get():

    html = render_template('header.html',name='login')
    html +=render_template('login.html',url = url_for('login_post'))
    html +=render_template('footer.html')
    return html

@app.post("/login")
def login_post():
    Login.teste()
    print(request.method)
    print(request.form['nome'])
    return "<p>Ola post teste!</p>"

@app.get("/easter_egg")
def easter_egg():
    return render_template('header.html',name='easter_egg')+render_template('easter_egg.html')+render_template('footer.html',scripts=[url_for('static',filename='konami.js')])

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello_world'))
    print(url_for('hello_world', next='/'))
    print(url_for('usuario_get', usuario='John Doe'))
    print(url_for('usuario_post', usuario='John Doe'))
    print(url_for('easter_egg'))