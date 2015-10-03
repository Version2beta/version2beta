var markdown = require('markdown-it');

var md = markdown();

var n = md.utils.normalizeLink;

md.utils.normalizeLink = function(url) {
  console.log(url);
  return n(url);
};

console.log(md.render("a [test](http://link.com)"));
