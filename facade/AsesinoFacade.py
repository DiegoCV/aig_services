from dao.entities.AsesinoDao import *
from dao.factory.FactoryDao import *
from dto.Asesino import *

class AsesinoFacade():
  
  def insert(self,asesino):
    asesinoDao = FactoryDao.getAsesinoDao()
    return asesinoDao.insert(asesino)
    
  
  def listAll(self):
    asesinoDao = FactoryDao.getAsesinoDao()
    return asesinoDao.listAll()
    

 