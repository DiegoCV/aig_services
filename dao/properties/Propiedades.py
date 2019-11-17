import yaml
import os

class Propiedades():
	
	def __init__(self):
		self.cfg
		with open(os.getcwd()+"\\dao\\properties\\propiedades.yml", 'r') as ymlfile:
			self.cfg = yaml.load(ymlfile)

	def get_gestor_default():
		return cfg['general']['gestor_default']

	def get_dbName_default():
		return cfg['general']['database_default']

	def get_usuario(database):
		return cfg[database]['username']

	def get_password(database):
		return cfg[database]['password']

	def get_host(database): 
		return cfg[database]['host']

	def get_port(database):
		return cfg[database]['port']
