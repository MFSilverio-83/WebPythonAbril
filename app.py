from flask import Flask, render_template

app = Flask("ola")

# raiz
@app.route('/')          # decorator - rotas
def ola():
    return "HomePage"

# nova aba
@app.route('/aluno')
def aluno():
    return render_template("ola.html")