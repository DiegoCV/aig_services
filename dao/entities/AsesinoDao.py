from dto.Asesino import *

class AsesinoDao():

  def __init__(self, conexion):
    self.cn = conexion
    
  def insert(self, asesino):
    id_asesino = None
    try:
      con = self.cn.database()
      con.child("revisiones").push(revision)
    except Exception as e: 
      print(e)
      #print('Got error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
      self.cn.close()
      return id_asesino
   
  def  listAll(self):
    asesinos = None
    try:
      asesinos = list()
      with  self.cn.cursor() as cursor:  
        sql = "SELECT `id_asesino`, `nombre_asesino` FROM `asesino` WHERE 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in range(0,len(result)):
          asesinos.append(Asesino(result[i]['id_asesino'],result[i]['nombre_asesino']))
      self.cn.commit()
    except Exception as e: 
      print(e)
      #print('Got error {!r}, errno is {}'.format(e, e.args[0]))
    finally:
      self.cn.close()
      return asesinos
      
