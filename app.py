# Importa de un paquete llamado flask, una clase llamada Flask
from flask import Flask, render_template
from entities.deseado import Deseado

# Se crea un objeto a partir del constructor de la clase Flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/deseados")
def deseados():
    deseados = Deseado.get_list()
    return render_template('deseados.html', deseados=deseados)

if __name__ == "__main__":
    app.run()