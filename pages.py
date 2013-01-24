import os
import io
import itertools
import yaml
import markdown2 as markdown
from flask import abort

md = markdown.MarkdownWithExtras()
#    safe_mode = False,
#    extensions = ['extra', 'codehilite'], )
#    output_format = "html5" )

class Page(object):
  file_suffix = ".yaml"

  @classmethod
  def load_from_file(self, name):
    file_name = name + self.file_suffix
    if not os.path.isfile(file_name):
      abort(404)
    mtime = os.path.getmtime(file_name)
    with io.open(file_name, encoding="utf8") as f:
      meta = ''.join(itertools.takewhile(unicode.strip, f))
      content = f.read()
    page = self(name, meta, md.convert(content))
    return page

  def __init__(self, name, meta, content, **kwargs):
    self.name = name
    self.meta = meta
    self.content = content
    for key, value in kwargs.items():
      setattr(self, key, value)

  def __getitem__(self, name):
    return self.meta[name]

  def meta(self):
    return yaml.safe_load(self.head) or {}
