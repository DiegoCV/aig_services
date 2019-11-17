class Asesino():
  
  def __init__(self, id_asesino,nombre_asesino):
    self.id_asesino = id_asesino
    self.nombre_asesino = nombre_asesino
    
  def getId_asesino(self):
    return self.id_asesino

  def setId_asesino(self,id_asesino):
    self.id_asesino = id_asesino

  def getNombre_asesino(self):
    return self.nombre_asesino

  def setNombre_asesino(self,nombre_asesino):
    self.nombre_asesino = nombre_asesino

  def toJSON(self):
    return {"id_asesino":str(self.id_asesino),"nombre_asesino":self.nombre_asesino}

