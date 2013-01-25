import os
import io
import glob
from datetime import datetime
import itertools
import yaml
import markdown2 as markdown
from flask import abort

md = markdown.MarkdownWithExtras()

class Page(object):
  file_suffix = ".yaml"

  @classmethod
  def get_meta_from_dir(self, name):
    pages = []
    for file_name in glob.glob(name + '/*' + self.file_suffix):
      d = datetime.fromtimestamp(os.path.getmtime(file_name))
      filedate = {
            "year": d.year, "month": d.month, "day": d.day,
            "hour": d.hour, "minute": d.minute, "second": d.second
          }
      page = self.load_from_file(file_name.replace(".yaml", ""))
      names = {
            "name": page.name,
            #"filename": file_name.replace("." + self.file_suffix, "")
            "filename": file_name.replace(self.file_suffix, "")
          }
      pages.append(dict(
            names.items() +
            page.meta.items() +
            filedate.items()
          ))
    return pages

  @classmethod
  def load_from_file(self, name):
    file_name = name + self.file_suffix
    if not os.path.isfile(file_name):
      abort(404)
    with io.open(file_name, encoding="utf8") as f:
      meta = ''.join(itertools.takewhile(unicode.strip, f))
      content = f.read()
    page = self(name, meta, md.convert(content))
    return page

  def __init__(self, name, meta, content, **kwargs):
    self.name = name
    self.meta = yaml.safe_load(meta) or {}
    self.content = content
    for key, value in kwargs.items():
      setattr(self, key, value)

  def __getitem__(self, name):
    return self.meta.get(name)
