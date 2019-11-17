'''
  La idea con esto es utilizar los dao como una forma para palidar nuestras seudo-entidades
  https://python-jsonschema.readthedocs.io/en/stable/
  jsonschema
   pip install jsonschema
'''
'''
from jsonschema import validate
 schema = {
     "type" : "object",
     "properties" : {
        "price" : {"type" : "number"},
         "name" : {"type" : "string"},
     },
 }
 correcto
 validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)

incorrecto
validate(instance={"name" : "Eggs", "price" : "Invalid"}, schema=schema)              

'''                     
class Asesino():
  
  @staticmethod    
    def validar(data): 
        return False

