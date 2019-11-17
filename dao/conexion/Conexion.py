from dao.conexion.conexiones.ConexionFirebase import *
from dao.properties.Propiedades import *

class Conexion():

  @staticmethod
  def obtenerConexion():
    return ConexionFirebase().obtener_conector(get_apiKey(),get_authDomain(),get_databaseURL(),get_storageBucket())