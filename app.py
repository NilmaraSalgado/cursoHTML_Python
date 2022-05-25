from flask import Flask, render_template, g
import sqlite3

DATABASE = "banco.bd"
SECRET_KEY = "chave"

#como usar o Flask. A linha abaixo já é uma aplicação Flask. gerando  premissas para se comunicar com um servidor.*/
app = Flask("Hello")
app.config.from_object(__name__)

#cliente do BD é nossa aplicação. Sendo uma arquit. cliente-servidor. Usando protocolo de Banco de Dados.
#python ja conhece essa comunicação. 
#Primeiro eu abro a conexao como banco. 

def conecta_db():
        return sqlite3.connect(DATABASE)

#lembre que as conexoes com o banco sao limitadas
@app.before_request
def antes_requisicao():
        #abrir a conexao guandando nesse local
        g.bd = conecta_db()

#agora preciso fechar a conexao
@app.teardown_request
def depois_requisicao(e):
        g.bd.close()

#agora vamos criar nossas rotas
@app.route("/")
#isso é nossa rota da tabela principal
def exibir_entradas():
        #aqui vou buscar o nome do BD
        #buscar no banco os posts
        sql = "SELECT titulo, texto, criado_em FROM entradas ORDER BY id DESC"
        cur = g.bd.execute(sql) #vou precisar guardar na variavel
        entradas = [ ]
        for titulo, texto, criado_em in cur.fetchall():
              entradas.append({"titulo": titulo, "texto": texto, "criado_em": criado_em})
        return render_template("layout.html", entradas=entradas)




