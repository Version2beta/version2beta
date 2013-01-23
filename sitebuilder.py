from flask import Flask, render_template
from flask_flatpages import FlatPages
from flaskext.markdown import Markdown

DEBUG = debug = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

@app.route('/')
def index():
  return "Hello World"

@app.route('/<path:path>/')
def page(path):
  page = pages.get_or_404(path)
  return render_template(page.get('template'), page = page)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
