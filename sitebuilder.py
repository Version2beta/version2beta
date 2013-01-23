import os
import io
import yaml
import werkzeug
import jinja2
import itertools
import markdown as markdown_module
import pygments.formatters
from flask import Flask, render_template, abort, url_for

DEBUG = debug = True
app = Flask(__name__)
app.config.from_object(__name__)
PYGMENTS_CSS = (pygments.formatters.HtmlFormatter(style='tango')
                    .get_style_defs('.codehilite'))

@app.template_filter()
def markdown(text):
  return markdown_module.markdown(text, extensions = ['codehilite', 'footnotes'])

class Page(object):
  root = os.path.join(app.root_path, u'pages')
  suffix = '.md'
  _cache = {}

  @classmethod
  def load(cls, year, name):
    filename = os.path.join(cls.root, year, name) + cls.suffix
    if not os.path.isfile(filename):
      abort(404)
    mtime = os.path.getmtime(filename)
    page, old_mtime = cls._cache.get(filename, (None, None))
    if not page or mtime != old_mtime:
      with io.open(filename, encoding='utf8') as fd:
        head = ''.join(itertools.takewhile(unicode.strip, fd))
        body = fd.read()
        page = cls(year, name, head, body)
        cls._cache[filename] = (page, mtime)
      return page

  @classmethod
  def years(cls):
    for year in os.listdir(cls.root):
      if year.isdigit():
        yield year

  @classmethod
  def articles_by_year(cls, year):
    directory = os.path.join(cls.root, year)
    if not os.path.isdir(directory):
      abort(404)
    for name in os.listdir(directory):
      if name.endswith(cls.suffix):
        yield cls.load(year, name[:-len(cls.suffix)])

  @classmethod
  def all_articles(cls):
    for year in cls.years():
      for article in cls.articles_by_year(year):
        yield article

  def __init__(self, year, name, head, body):
    self.year = year
    self.name = name
    self.head = head
    self.body = body

  @werkzeug.cached_property
  def meta(self):
    return yaml.safe_load(self.head) or {}

  def __getitem__(self, name):
    return self.meta[name]

  @werkzeug.cached_property
  def html(self):
    return markdown(self.body)

  def url(self, **kwargs):
    return url_for('article', year=int(self.year), name=self.name, **kwargs)

@app.route('/')
def index():
  return "Hello World"

@app.route('/about/')
def about():
  return render_template('about.html', page = Page.load('', 'about'))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
