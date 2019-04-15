from flask import render_template
from app import app 
from .request import get_sources,get_top_headlines

#create a route decorator
@app.route('/')
#define the view function
def index() :
  '''
  View root page function that returns the index page and its data
  '''

  #get sources
  sources = get_sources()
  print(sources)
  title = 'Home - Welcome to the best movie review website online '
  return render_template('index.html', title = title, sources = sources)

@app.route('/source/<source>')
def Top_Headlines(source) :
  '''
  view Top_Headlines page function that returns the Top_Headlines from a source details page and its data 
  '''
  
  Top_headlines = get_top_headlines(source)
  print(Top_headlines)

  return render_template('Top_headlines.html', Top_headlines = Top_headlines)
  
  