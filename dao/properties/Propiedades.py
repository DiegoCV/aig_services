import yaml
import os

class Propiedades():

	#Esto es para efectos de pruebas locales, hay que cambiarlo despues a variables de entorno
	def __init__(self):
		with open(os.getcwd()+"\\dao\\properties\\propiedades.yml", 'r') as ymlfile:
			self.cfg = yaml.load(ymlfile)

	def get_apiKey(self):
		return self.cfg['aig_bd']['apiKey']

	def get_authDomain(self):
		return self.cfg['aig_bd']['authDomain']

	def get_databaseURL(self):
		return self.cfg['aig_bd']['databaseURL']

	def get_storageBucket(self):
		return self.cfg['aig_bd']['storageBucket']

	


	
