from flask import Flask, request, Response, jsonify
from controller.asesino.AsesinoController import *
from entities.asesino.Asesino import *
from util.Pregonero import *

app = Flask(__name__)

@app.route('/asesino/insertar', methods=['POST'])
def insertarAsesino():
    data = request.get_json()
    if Asesino.validar(data):
            asesinoController = AsesinoController()
            asesino = asesinoController.insertar(data)
            return responder(asesino)
    else:
        return responderErrorFormatData()
    
@app.route('/asesino/listar', methods=['GET'])
def listarAsesino():
    asesinoController = AsesinoController()
    return jsonify(asesinoController.listarTodo())
    
app.run()