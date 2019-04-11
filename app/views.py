from flask import render_template
from app import app 

#create a route decorator
@app.route('/')
#define the view function
def index() :
  '''
  View root page function that returns the index page and its data
  '''
  return render_template('index.html')