from flask import Flask

app = Flask("ola")

@app.route('/')          # decorator - rotas
def ola():
    return "Olá Mundo"