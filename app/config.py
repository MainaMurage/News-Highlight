class Config :
  '''
  General configuration parent class 
  '''
  NEWS_HIGHLIGHT_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
  TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apikey={}' 


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

