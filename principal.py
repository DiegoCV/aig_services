import os.path
from flask import Flask, request, Response, jsonify
from controller.asesino.AsesinoController import *

def root_dir():
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	content = get_file('index.html')
	return Response(content, mimetype="text/html")

@app.route('/asesino/insertar', methods=['POST'])
def insertarAsesino():
    asesinoController = AsesinoController()
    return jsonify(asesinoController.insertar(request.form['id_asesino'],request.form['nombre_asesino']))
    
@app.route('/asesino/listar', methods=['GET'])
def listarAsesino():
    asesinoController = AsesinoController()
    return jsonify(asesinoController.listarTodo())
    
app.run()