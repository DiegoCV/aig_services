import pyrebase

class ConexionFirebase:
	
	@staticmethod
	def obtener_conector(apiKey, authDomain, databaseURL, storageBucket):
		config = {
  			"apiKey": apiKey,
		  	"authDomain": authDomain,
		 	"databaseURL": databaseURL,
		  	"storageBucket": storageBucket
		}
		return pyrebase.initialize_app(config)