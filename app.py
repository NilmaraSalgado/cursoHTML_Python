from flask import Flask, render_template

#como usar o Flask. A linha abaixo já é uma aplicação Flask. gerando  premissas para se comunicar com um servidor.*/
app = Flask("Hello")

#notacao que quero que 1 url chame uma funcao
#ambiente ja com as bibliotecas em requeriments
@app.route("/hello")
#criaçao da funcao
def hello():
        #chamando o arquivo template.html
        return render_template("hello.html")
