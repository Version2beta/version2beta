import pygments.formatters
from flask import Flask, render_template, abort, url_for, json
from pages import Page

DEBUG = debug = True
app = Flask(__name__)
app.config.from_object(__name__)
PYGMENTS_CSS = (
    pygments.formatters.HtmlFormatter(style='tango').get_style_defs('.codehilite') )

@app.route('/')
def index():
  return "Hello World"

@app.route('/<page>')
def about(page):
  return render_template('pages.html', page = Page.load_from_file('pages/' + page))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
