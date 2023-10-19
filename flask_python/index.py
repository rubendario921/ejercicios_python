# En este apartado presento un catalogo de programas que uso con Flask para el desarrollo web
from flask import Flask, render_template, Request

# Nombre de la Aplicacion
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/operaciones_logicas")
def operaciones_logicas():
    return render_template("operaciones_logicas.html")


# @app.route("/par_impar", methods=["POST"])
# def par_impar():
#     num1 = int(Request.form["num1"])
#     if num1 > 0:
#         resultado = "El número ingresado es par"
#     else:
#         resultado = "El número ingresado es impar"

#         return render_template()


if __name__ == "__main__":
    app.run(debug=True)
