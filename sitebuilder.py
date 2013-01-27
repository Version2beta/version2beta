import sys
from datetime import datetime
import pygments.formatters
from flask import Flask, render_template, abort, url_for, json, redirect
from flask_frozen import Freezer
from pages import Page

DEBUG = debug = True
app = Flask(__name__)
app.config.from_object(__name__)
#FREEZER_BASE_URL = "http://version2beta.com/"
freezer = Freezer(app)

@app.route('/')
def index():
  return redirect(url_for('articles'))

@app.route('/articles/')
def articles():
  return ( render_template('articles.html',
           pages = Page.get_meta_from_dir('articles')),
           200,
           {'Content-Type': 'text/html'} )

@app.route('/articles/<page>/')
def article(page):
  return ( render_template('article.html', page = Page.load_from_file('articles/' + page)),
           200,
           {'Content-Type': 'text/html'} )

@app.route('/<page>/')
def pages(page):
  return ( render_template('pages.html', page = Page.load_from_file('pages/' + page)),
           200,
           {'Content-Type': 'text/html'} )

@app.route('/atom.xml')
def feed():
  return render_template('feed.xml',
      pages = Page.get_meta_from_dir('articles'),
      now = datetime.now()), 200, {'Content-Type': 'application/xml'}

@app.route('/pygments.css')
def pygments_css():
  return ( 
      pygments.formatters.HtmlFormatter(style='tango').get_style_defs('.codehilite'),
      200,
      {'Content-Type': 'text/css'} )

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

@freezer.register_generator
def article():
  for page in Page.get_meta_from_dir('articles'):
    yield { 'page': page['name'] }

@freezer.register_generator
def pages():
  for page in Page.get_meta_from_dir('pages'):
    yield "pages", { "page": "/" + page['name'] }

if __name__ == '__main__':
  if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
  else:
    app.run(host='0.0.0.0', port=8000)
