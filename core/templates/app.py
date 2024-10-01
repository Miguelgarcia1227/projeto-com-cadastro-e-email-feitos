from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import hashlib

app = Flask(__name__)

def conectar_banco():
    conn = sqlite3.connect('usuarios.db')
    return conn



        return redirect(url_for('sucesso'))
    return render_template('cadastro.html')

@app.route('/sucesso')
def sucesso():
    return "Cadastro realizado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
