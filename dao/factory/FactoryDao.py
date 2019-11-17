from dao.conexion.Conexion import *
from dao.entities.AsesinoDao import *


class FactoryDao():
    
    @staticmethod    
    def getAsesinoDao():
        conexion = Conexion()
        return AsesinoDao(conexion.obtenerConexion())

 