from flask import render_template
from app import app 
from .request import get_sources

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

@app.route('/movie/<int:movie_id>')
def movie(movie_id) :
  '''
  view movie page function that returns the movie details page and its data 
  '''
  return render_template('movie.html', id = movie_id)
  