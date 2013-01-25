import pygments.formatters
from flask import Flask, render_template, abort, url_for, json, redirect
from pages import Page

DEBUG = debug = True
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
  return redirect(url_for('articles'))

@app.route('/articles')
def articles():
  return render_template('articles.html', pages = Page.get_meta_from_dir('articles'))

@app.route('/articles/<page>')
def article(page):
  return render_template('article.html', page = Page.load_from_file('articles/' + page))

@app.route('/<page>')
def about(page):
  return render_template('pages.html', page = Page.load_from_file('pages/' + page))

@app.route('/pygments.css')
def pygments_css():
  return ( 
      pygments.formatters.HtmlFormatter(style='tango').get_style_defs('.codehilite'),
      200,
      {'Content-Type': 'text/css'} )

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
