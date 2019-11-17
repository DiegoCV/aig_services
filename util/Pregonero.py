from flask import jsonify
from util.Firma import * 
firma = Firma()

def responder(algo):
	return jsonify({'status' : '1','message':'Al parecer no eres tan malo despues de todo','algo':algo})

def responderError():
	return jsonify({'status' : '0','message':'Tienes un mal dia'})

def reponderLogin(usuario):
	return jsonify({'status' : '1','jwt':firma.obtener_firma(usuario)})

def reponderTEST(usuario,sesiones):
	return jsonify({'status' : '1','sesion':sesiones,'usuario':usuario})