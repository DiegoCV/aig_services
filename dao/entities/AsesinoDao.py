from dto.Asesino import *

class AsesinoDao():

  def __init__(self, conexion):
    self.cn = conexion
    
  def insert(self, asesino):
    id_asesino = None
    mit = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjhhMzY5M2YxMzczZjgwYTI1M2NmYmUyMTVkMDJlZTMwNjhmZWJjMzYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZmVlZG1lLWEzNTE2IiwiYXVkIjoiZmVlZG1lLWEzNTE2IiwiYXV0aF90aW1lIjoxNTc0MDIzNzMzLCJ1c2VyX2lkIjoiVmJnSW43STdwT1VZYUdZZDhqM05iRk04ZkV0MiIsInN1YiI6IlZiZ0luN0k3cE9VWWFHWWQ4ajNOYkZNOGZFdDIiLCJpYXQiOjE1NzQwMjM3MzMsImV4cCI6MTU3NDAyNzMzMywiZW1haWwiOiJyZXN0QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJyZXN0QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.E2xuoim7C-IKNhUqSoDhIN4F2gzJ4kEFHegULZ8zNrVhaLQOYLtZuqODkB_jTKzm6ARL82jg32Z3biDwVERZF1wYQ1nkJi-iohq361Z1rqXs1wjLxGISEk8lHbi0zyz-G1OutqSPiE_gsejwBz0p36jZAYkog8zmi9R0Dy59Kc4JdC_GYFTWvjqqQg0a5DReaYPuwqkXt8bA-NxTvuFNrHef1tfvhHiNGf5ZmQdmGUJAMpm2RDCyKikVQFIyyv9LIlj_kIUZfK6oDq71K6rjotCfITPzS3HNcFEpe8heQOu_EoDDMyaa_fScQUMmCzRIxY2soSJqsIUn2rRTh2TkcA"
    try:
     # self.autenticarme()
      #auth =  self.cn.auth()
      #ff = auth.send_email_verification(mit)
      storage = self.cn.storage()
      
      id_asesino = storage.child("organigrama.jpg").get_url()
     # print(ff)
     # con = self.cn.database()
      #con.child("restaurante").push(asesino, mit)
      #ñid_asesino = con.child("restaurante").get(token=mit)
     # id_asesino = ñid_asesino.val()
    except Exception as e: 
      print("MI EXEPCION")
      print(e)
    finally:
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


  ''' Esto es muy interesante, al parecer loguerse si sirve para algo. '''
  ''' La unica manera de solicitar un servicio en firebase es autenticandose primero'''    
  def  autenticarme(self):
    mi_token = None
    try:
      auth =  self.cn.auth()
      # Log the user in
      user = auth.sign_in_with_email_and_password("rest@gmail.com", "123456")
      print(user)
      mi_token = user['idToken']
    except Exception as e: 
      print(e)
    finally:
      return mi_token
      
  # Get a reference to the auth service
