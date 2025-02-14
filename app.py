from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("hello_there.html")  # Aqui não precisa de 'name'

@app.route("/hello/<name>")
def hello_there(name):
    return render_template("hello_there.html", name=name)  # Aqui passamos 'name' para o template
 
@app.route("/hi/")
def hi_there():
    return "Hi fulano"


@app.route("/portifolio/")
def fale_conosco():
    return render_template('index.html')

@app.route("/formulario/")
def chamar_formulario():
    return render_template('formulario.html')

@app.route("/enviar", methods =["POST"])
def enviar_formulario():
    
    nome = request.form["nome"]
    mensagem = request.form["mensagem"]


    return render_template('formulario.html', nome=nome, mensagem=mensagem)


if __name__ == "__main__":
    app.run(debug=True)



