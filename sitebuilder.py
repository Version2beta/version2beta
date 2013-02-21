import os
import sys
from datetime import datetime
import pygments.formatters
from flask import Flask, render_template, abort, url_for, json, redirect
from flask_frozen import Freezer
from pages import Page
import boto
from boto.s3.key import Key

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

@app.route('/articles/<page>/readable/')
def note(page):
  return ( render_template('note.html', page = Page.load_from_file('articles/' + page)),
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
  return render_template('pages.html', page = Page.load_from_file('pages/404')), 404

@freezer.register_generator
def register_pages():
  for page in Page.get_meta_from_dir('articles'):
    yield "article", { 'page': page['name'] }
    yield "note", { 'page': page['name'] }
  for page in Page.get_meta_from_dir('pages'):
    yield "pages", { "page": "/" + page['name'] }

def deploy():
  print "Building the site."
  freezer.freeze()
  homedir = os.path.expanduser('~')
  with open(homedir + '/.aws/access_key') as  f:
    access_key = f.read()
  with open(homedir + '/.aws/secret_key') as  f:
    secret_key = f.read()
  s3 = boto.connect_s3(access_key, secret_key)
  bucket = s3.lookup('version2beta.com')
  print "Sending files to S3:"
  for deploydir, subdirectories, filenames in os.walk('build'):
    for filename in filenames:
      key = Key(bucket)
      key.key = os.path.join(deploydir + "/" + filename).replace("build/", "")
      print "  " + key.key
      with open("build/" + key.key) as f:
        key.set_contents_from_file(f)
      del key

if __name__ == '__main__':
  if len(sys.argv) < 2:
    app.run(host='0.0.0.0', port=8000)
  elif sys.argv[1] == "build":
    freezer.freeze()
  elif sys.argv[1] == "deploy":
    deploy()
