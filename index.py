from flask import Flask

# Nombre de la Aplicacion
app = Flask(__name__)

@app.route('/')
def home():
    return 'Pagina de Inicio'

if __name__ == '__main__':
    app.run(debug=True)