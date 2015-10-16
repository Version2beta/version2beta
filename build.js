var Metalsmith = require('metalsmith'),
  assets = require('metalsmith-assets'),
  branch = require('metalsmith-branch'),
  markdown = require('metalsmith-markdown-remarkable'),
  moment = require('moment'),
  tags = require('metalsmith-tags'),
  collections = require('metalsmith-collections'),
  feed = require('metalsmith-feed'),
  permalinks = require('metalsmith-permalinks'),
  snippet = require('metalsmith-snippet'),
  layout = require('metalsmith-layouts');

md = markdown('full', {
  html: true
}),

//primary site build
Metalsmith(__dirname)
  .metadata({
    site: {
      title: 'version2beta',
      url: 'http://version2beta.com/',
      author: 'Rob Martin'
    }
  })
  .use(md)
  .use(snippet())
  .use(collections({
    articles: {
      pattern: 'articles/**.html',
      sortBy: 'published',
      reverse: true
    }
  }))
  .use(branch('articles/**.html')
      .use(permalinks({
        pattern: 'articles/:title',
        relative: false
      }))
  )
  .use(branch('*.html')
    .use(permalinks({
      pattern: ':title',
      relative: false
    }))
  )
  .use(tags({
    collection: 'articles',
    handle: 'tags',
    path:'topics/:tag/index.html',
    layout:'topics.jade',
    sortBy: 'published',
    reverse: true,
    skipMetadata: false
  }))
  .use(layout({
    engine: 'jade',
    moment: moment,
    default: 'article.jade'
  }))
  .use(feed({
    collection: 'articles'
  }))
  .use(assets({
    source: './assets',
    destination: '.'
  }))
  .destination('./build-content')
  .build(function (err) {
    if (err) {
      console.log(err);
    }
    else {
      console.log('Site build complete! Because you are a magical unicorn.');
    }
  });

//build again for readable articles
Metalsmith(__dirname)
  .source('./src/articles')
  .use(md)
  .use(snippet())
  .use(branch('**.html')
    .use(permalinks({
      pattern: ':title',
      relative: false
    }))
  )
  .use(layout({
    engine: 'jade',
    moment: moment,
    default: 'readable.jade'
  }))
  .destination('./build-content/readable/articles')
  .build(function (err) {
    if (err) {
      console.log(err);
    }
    else {
      console.log('Readable files completed!');
    }
  });
