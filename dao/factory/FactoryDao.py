from dao.conexion.Conexion import *
from dao.entities.AsesinoDao import *


class FactoryDao():
    
    @staticmethod    
    def getAsesinoDao(): 
        return AsesinoDao(Conexion.obtenerConexion())

 