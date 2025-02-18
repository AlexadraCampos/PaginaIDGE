from flask import Flask, render_template, request, jsonify 
from idgc import IDGC
import re  

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("hello_there.html")  # Aqui não precisa de 'name'

@app.route("/hello/<name>")
def hello_there(name):
    return render_template("hello_there.html", name=name)  # Aqui passamos 'name' para o template
 

@app.route("/portifolio/")
def fale_conosco():
    return render_template('index.html')

# Rota frontend
@app.route("/formulario/")
def chamar_formulario():
    return render_template('formulario.html')

# Rota para validar cpf via POST
@app.route("/validar", methods=["POST"])
def validar():
        
    identificador = request.form["chave"] 
    categoria = request.form["categoria"]
    idgc = IDGC() 
    if categoria == "CPF":
        valido = idgc.Brazil_CPF_Validator(identificador)  
    elif categoria == "CNPJ":
        valido = idgc.Brazil_CNPJ_Validator(identificador)
    elif categoria == "DNI":
        valido = idgc.Argentina_DNI_Validator(identificador)
    elif categoria == "CUIL":
        valido = idgc.Argentina_CUIL_Validator(identificador)

    return render_template('formulario.html', identificador=identificador, valido=valido)


# @app.route("/Validar", methods =["POST"])
# def enviar_formulario():
    
#     nome = request.form["nome"]
#     mensagem = request.form["mensagem"]


#     return render_template('formulario.html', nome=nome, mensagem=mensagem)


# Inicio do servidor flask
if __name__ == "__main__":
    app.run(debug=True)



