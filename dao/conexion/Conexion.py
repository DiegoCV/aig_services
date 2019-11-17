from dao.conexion.conexiones.ConexionFirebase import *
from dao.properties.Propiedades import *

class Conexion(object):

  __instance = None
  mi_conexion = None
  p = Propiedades()

  def obtenerConexion(self):
    if self.mi_conexion is None:
      self.mi_conexion = ConexionFirebase().obtener_conector(self.p.get_apiKey(), self.p.get_authDomain(), self.p.get_databaseURL(), self.p.get_storageBucket())
    return self.mi_conexion

  def __new__(cls):
    if Conexion.__instance is None:
      Conexion.__instance = object.__new__(cls)
    return Conexion.__instance
			