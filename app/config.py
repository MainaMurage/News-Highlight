class Config :
  '''
  General configuration parent class 
  '''
  pass # denote null block of code 


class ProdConfig(Config) :
  '''
  Production configuration child class
  
  Args: 
    config : The parent configuration class with General configuration settings
  '''
  pass

class DevConfig(Config) :
  '''
  Development configuration child class 
  '''
  DEBUG = True #enable debug mode in my app 

