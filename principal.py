from flask import Flask, request, Response, jsonify
from controller.asesino.AsesinoController import *
from dto.Asesino import *
from util.Pregonero import *

app = Flask(__name__)

@app.route('/asesino/insertar', methods=['POST'])
def insertarAsesino():
    data = request.get_json()
    print(data)
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


'''En vista debe existir un scritp que controle el tiempo de sesion, unos minutos antes de la hora el deberia actualizar el token'''
    
app.run()