from app import app 
#import the module that will help create a connection to the API URL and send a request
#import json modules that will format the JSON response to a dict
import urllib.request, json
from .models import source,top_headlines

Source = source.Source
Top_Headlines = top_headlines.Top_Headlines

#get the api key
api_key =app.config['NEWS_HIGHLIGHT_API_KEY']

#get the source base url
base_url = app.config["NEWS_HIGHLIGHT_API_BASE_URL"]

#get the top headlines url
headlines_url = app.config["TOP_HEADLINES_URL"]

def get_sources() :
  '''
  get the json response to our url request 
  '''
  get_sources_url = base_url.format(api_key)

  with urllib.request.urlopen(get_sources_url) as url :
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    source_results =  None 

    if get_sources_response['sources'] :
      source_results_list = get_sources_response['sources']
      source_results = process_source_results(source_results_list)

  return source_results 

def process_source_results(source_list) :
  '''
  process source result and transform them to a list of objects
  '''
  source_results = []
  for source_item in source_list :
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')
    category = source_item.get('category')
    language = source_item.get('language')
    country = source_item.get('country')

    source_object = Source(id, name, description, url, category, language, country)
    source_results.append(source_object)

  return source_results

def get_top_headlines(source) :
  get_top_headlines_url = headlines_url.format(source, api_key)

  with urllib.request.urlopen(get_top_headlines_url) as url :
    top_headlines_data = url.read()
    top_headlines_response = json.loads(top_headlines_data)

    top_headlines_object = None 

    if top_headlines_response['articles'] :
      author = top_headlines_response.get('author')
      title = top_headlines_response.get('title')
      description = top_headlines_response.get('description')
      url = top_headlines_response.get('url')
      urlToImage = top_headlines_response.get('urlToImage')
      publishedAt = top_headlines_response.get('publishedAt')
      content = top_headlines_response.get('content')

      top_headlines_object = Top_Headlines(author, title, description, url, urlToImage, publishedAt, content) 

    return(top_headlines_object)
  




