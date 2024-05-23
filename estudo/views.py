from estudo import app
from flask import render_template, url_for

@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/Planos/')
def planos():
    return render_template('planos.html')

@app.route('/Login/')
def login():
    return render_template('login.html')

app.route('/Registrar/')
def registrar():
    return render_template('registrar.html')