# En este apartado presento un catalogo de programas que uso con Flask para el desarrollo web
from flask import Flask, render_template, Request

# Nombre de la Aplicación
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")


if __name__ == "__main__":
    app.run(debug=True)
