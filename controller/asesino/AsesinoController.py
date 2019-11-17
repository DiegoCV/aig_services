from facade.AsesinoFacade import *

class AsesinoController():  

	def insertar(self,asesino):
		asesino_facade = AsesinoFacade()
		return asesino_facade.insert(asesino)

	def listarTodo(self):
		asesino_facade = AsesinoFacade()
		return asesino_facade.listAll()
		
