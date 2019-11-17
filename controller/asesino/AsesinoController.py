from dto.Asesino import *
from facade.AsesinoFacade import *

class AsesinoController():  

	def insertar(self,id_asesino, nombre_asesino):
		asesino = Asesino(id_asesino,nombre_asesino)
		asesino_facade = AsesinoFacade()
		return asesino_facade.insert(asesino)

	def listarTodo(self):
		asesino_facade = AsesinoFacade()
		asesinos = asesino_facade.listAll()
		return {"status": "1", "asesinos": self.tamizarList(asesinos)}

	def tamizarList(self,asesinos):
		rta = []
		for asesino in asesinos:
			rta.append(asesino.toJSON())
		return rta
