
var assert = require('assert');
var equal = require('assert-dir-equal');
var Metalsmith = require('metalsmith');
var markdown = require('..');

describe('metalsmith-markdown', function(){
  it('should convert markdown files with no parameters', function(done){
    Metalsmith('test/fixtures/basic')
      .use(markdown())
      .build(function(err){
        if (err) return done(err);
        equal('test/fixtures/basic/expected', 'test/fixtures/basic/build');
        done();
      });
  });

  it('should convert markdown files with presets', function(done){
    Metalsmith('test/fixtures/preset')
      .use(markdown('default'))
      .build(function(err){
        if (err) return done(err);
        equal('test/fixtures/preset/expected', 'test/fixtures/preset/build');
        done();
      });
  });

  it('should convert markdown files with options', function(done){
    Metalsmith('test/fixtures/options')
      .use(markdown({ html: true }))
      .build(function(err){
        if (err) return done(err);
        equal('test/fixtures/options/expected', 'test/fixtures/options/build');
        done();
      });
  });

  it('should convert markdown files with preset and options combination', function(done){
    Metalsmith('test/fixtures/combo')
      .use(markdown('default', { typographer: true }))
      .build(function(err){
        if (err) return done(err);
        equal('test/fixtures/combo/expected', 'test/fixtures/combo/build');
        done();
      });
  });

  it('should give access to markdown parser', function(done){
    var md = markdown('zero');

    md.parser.enable('emphasis');

    Metalsmith('test/fixtures/parser')
      .use(md)
      .build(function(err){
        if (err) return done(err);
        equal('test/fixtures/parser/expected', 'test/fixtures/parser/build');
        done();
      });
  });

  it('should be able to use a plugin', function(done){
    var md = markdown('default');

    md.parser.use(require('markdown-it-abbr'));

    Metalsmith('test/fixtures/plugin')
      .use(md)
      .build(function(err){
        if (err) return done(err);
        equal('test/fixtures/plugin/expected', 'test/fixtures/plugin/build');
        done();
      });
  });
});
