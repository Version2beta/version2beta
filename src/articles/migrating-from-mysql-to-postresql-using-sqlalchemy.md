---
pagetitle: Migrating from MySQL to PostgreSQL using SQLAlchemy
longtitle: Our codebase used SQLAlchemy on MySQL, and we moved to PostgreSQL. There were some gotchas. This post compiles our notes along with SQLAlchemy author Mike Bayer's comments and clarifications.
author: Rob Martin
published: 2013-05-13 08:00
snippet: This is basically a guest blog post. The content was created almost entirely by Paul Morel (owner of Tartan Solutions) and Mike Bayer (author of SQLAlchemy and other fine Python libraries.) I was invited to compile and edit the conversation.
---

In this blog post, my coworker and boss Paul Morel has just completed a migration from MySQL to PostgreSQL on a codebase using SQLAlchemy. Paul has collected together some gotchas and WTF's for posterity, and very graciously asked me if I'd like to post them to my blog - an opportunity I jumped at.

In order to round out the conversation, I also asked Mike Bayer[^mikebayer] to review Paul's notes and provide any commentary he thinks may be helpful. Mike is the author of SQLAlchemy, as well as a number of other powerful Python tools.

Paul's notes, and Mike's responses, are interleaved below.

**Paul Morel**:

SQLAlchemy does not wrap the Boolean column for MySQL so that 1's are `True` and 0's are `False`.  This means that all code must be updated to change conditions from `== 1` to `== True` and `== 0` to `== False`.  Postgres does this right by having booleans while MySQL only has tinyint.  The SQLAlchemy class should probably mask this from developer so the Boolean column only returns `True`, `False`, and `None`.

**Mike Bayer**:

> SQLAlchemy does not wrap the Boolean column for MySQL so that 1s = True and 0s = False.  This means that all code must be updated to change conditions from == 1 to == True and == 0 to == False.

The SQLAlchemy Boolean type specifically handles the True/False constants, and translates them to 1 and 0 on the *backend* side, not the public side, for backends that don't have a native boolean of their own, e.g. MySQL.  However, if your code deals with all == 1 and == 0, the first thing to note is that the True/False constants in Python *are* the integers 1 and 0 (try True == 1, type(True).__mro__ to see).  The second thing is that SQLA's Boolean type when used against psycopg2 doesn't do any coercion, and psycopg2 doesn't either, but for any type you can add whatever coercion you like using TypeDecorator:

```
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, Boolean, TypeDecorator

class CoerceBool(TypeDecorator):
  impl = Boolean

  def process_bind_param(self, value, dialect):
    if value is not None:
      return bool(value)
    else:
      return None

t1 = Table('t1', MetaData(), Column('boolvalue', CoerceBool))

e = create_engine("postgresql://scott:tiger@localhost/test", echo=True)
conn = e.connect()
trans = conn.begin()

t1.create(conn)
conn.execute(t1.insert(), {'boolvalue': 1})
assert conn.scalar(t1.select()) is True
assert conn.scalar(t1.select().where(t1.c.boolvalue == 1)) is True

trans.rollback()
```

> Postgres does this right by having booleans while MySQL only has tinyint.  The SQLAlchemy class should probably mask this from developer so the Boolean column only returns True, False, and None.

I don't understand this statement since this is exactly what the Boolean type *does* do.  Boolean only returns True, False and None, assuming you're using it against a boolean column on postgresql.  If you point it at an int, that's the wrong usage.  Use a TypeDecorator around Integer for that.

**Paul Morel**:

SQLAlchemy does not alias the `func.ifnull` function as `COALESCE` for Postgres.  So, any code using the `ifnull` method breaks until it is changed to `func.coalesce()`.  You can use `func.coalesce` with MySQL so it is safer to start with that but any legacy code still using `ifnull` must be changed for Postgres use.

**Mike Bayer**:

> SQLAlchemy does not alias the `func.ifnull` function as `COALESCE` for Postgres.  So, any code using the `ifnull` method breaks until it is changed to `func.coalesce()`.

You can redefine any func.<xyz> in any way you'd like per specific backend.  It's easier in 0.8 which I recommend for new projects:

```
from sqlalchemy.sql.functions import GenericFunction
from sqlalchemy.ext.compiler import compiles
from sqlalchemy import create_engine, func

class IfNull(GenericFunction):
  name = 'ifnull'

@compiles(IfNull, "postgresql")
def coalesce(element, compiler, **kw):
  return compiler.process(func.coalesce(*element.clauses), **kw)

e = create_engine("postgresql://scott:tiger@localhost/test", echo=True)
assert e.scalar(func.ifnull(None, 8)) == 8
```

**Paul Morel**:

MySQL treats Text column types as `BLOB`.  So migrating data from MySQL to Postgres introduces `\015\012\` characters in place of line break characters. If the data stored in a Text type column all have lengths under 255, the column can be converted to `varchar(255)` before trying to migrate the data.  If not, the binary characters need to be corrected after migration.

**Mike Bayer**:

> MySQL treats Text column types as `BLOB`.  So migrating data from MySQL to Postgres introduces `\015\012\` characters in place of line break characters.

I'm not aware of any reason why that would be true.   Whatever data you have in your MySQL BLOB comes out just as it is, and goes straight into the PG TEXT column in just the same way.   There shouldn't be any line break conversion behavior.

> If the data stored in a Text type column all have lengths under 255, the column can be converted to `varchar(255)` before trying to migrate the data.

Postgresql supports VARCHAR of any length, including unlimited.   So feel free to declare a column as VARCHAR on PG, without a length:

```
from sqlalchemy import *
import random

t = Table('t1', MetaData(), Column('data', String))

e = create_engine("postgresql://scott:tiger@localhost/test", echo=True)

data = "".join(chr(random.randint(ord('A'), ord('Z'))) for i in xrange(10000))
conn = e.connect()
trans = conn.begin()

t.create(conn)
conn.execute(t.insert(), {"data": data})

assert conn.scalar(t.select()) == data

trans.rollback()
```

> If not, the binary characters need to be corrected after migration.

This sounds like something that's local to your own software.

**Paul Morel**:

There is no self correcting auto increment feature for Postgres since auto increment is achieved through sequences.  Therefore, after migrating data you must update all sequences to the proper position so the nextval() command will return a valid number and not cause key violations.  I had to write a routine that would update all sequences to their latest max corresponding value for the table key where they are used.

**Mike Bayer**:

This is true.

**Paul Morel**:

Granting rights to a database for a user does not actually do much.  You must grant rights on all tables specifically.  In addition, if you have auto increment sequences being used, you must also grant `USAGE` permission on the sequences.  While these can all be granted at the schema level, they do require several commands and it is rather opaque when coming from the simplicity of the MySQL security model.

**Mike Bayer**:

Wow I feel the total opposite, MySQL's model which inexplicably takes into account the "hostname" and weird things like "user@*.*" has never made sense to me. PG's is clear, and there's no need for a per table grant as he says, just do this:

```
GRANT ALL PRIVILEGES ON DATABASE <database name> TO <username>
```

The syntax diagram at [http://www.postgresql.org/docs/9.0/static/sql-grant.html](http://www.postgresql.org/docs/9.0/static/sql-grant.html) shows all the options.

**Paul Morel**:

Database objects in Postgres are all expected to be lowercase.  If for some reason, you chose to use non-lowercase values for table or field names you must enclose them in double quotes.  So all of you Oracle and SQL Server developers that use all upper or camel case are going to be in for an unpleasant surprise.  SQLAlchemy handles this for you but if you have any hand written SQL those queries will need to be updated.  If you leave a field or table unquoted it will automagically get converted to lowercase when trying to access the database objects.  For a database that strives to not do magic things, this one is sort of puzzling.

**Mike Bayer**:

> Database objects in Postgres are all expected to be lowercase.

Totally untrue. Postgresql will consider a name to be case insensitive if it isn't quoted, that is `CREATE TABLE SomeTable ()`, which causes the symbol "SomeTable" to be represented as "sometable", and it will match any casing in any statement. If you quote the name, i.e. 'CREATE TABLE "SomeTable"', now it's case sensitive and has to be specified as "SomeTable" in any statement.

[http://www.postgresql.org/docs/9.2/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS](http://www.postgresql.org/docs/9.2/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS)

Quoting an identifier also makes it case-sensitive, whereas unquoted names are always folded to lower case. For example, the identifiers FOO, foo, and "foo" are considered the same by PostgreSQL, but "Foo" and "FOO" are different from these three and each other. (The folding of unquoted names to lower case in PostgreSQL is incompatible with the SQL standard, which says that unquoted names should be folded to upper case. Thus, foo should be equivalent to "FOO" not "foo" according to the standard. If you want to write portable applications you are advised to always quote a particular name or never quote it.)"

> If for some reason, you chose to use non-lowercase values for table or field names you must enclose them in double quotes.

See documentation above.

> So all of you Oracle and SQL Server developers that use all upper or camel case are going to be in for an unpleasant surprise.

This is an odd statement because Oracle and SQL Server have nearly the same behavior - Oracle instead will fold case to UPPERCASE in the absence of quotes, SQL Server will maintain the casing you specify without quotes but still applies case sensitivity based on whether or not you supplied quotes (which also, conveniently, are the bracket character [] up until very recent versions).

MySQL IMO has by far the most unreasonable and outrageous casing behavior, basing it on *the operating system in use* :

[http://dev.mysql.com/doc/refman/5.0/en/identifier-case-sensitivity.html](http://dev.mysql.com/doc/refman/5.0/en/identifier-case-sensitivity.html)

> SQLAlchemy handles this for you but if you have any hand written SQL those queries will need to be updated.

If your schemas are created using case insensitive names, that is without quotes, then you can refer to any kind of casing convention you'd like in your statements. No need to update hand written statements:

```
test=> CREATE TABLE FooTable (SomeCrazyCasING integer);
CREATE TABLE
test=> INSERT INTO fooTABLE (someCRAZYcasing) VALUES (3);
INSERT 0 1
test=> SELECT SOMECRAZYCASiNG FROM FOOTABLE;
somecrazycasing
---------------
              3
        (1 row)
```

>  If you leave a field or table unquoted it will automagically get converted to lowercase when trying to access the database objects.  For a database that strives to not do magic things, this one is sort of puzzling.

Because the unquoted identifier name is not actually uppercase or lowercase, it's "case insensitive".  Any case matches it, schema inspection tools will display it as lowercase and it will be represented in the information schema views with lowercase names (this is the one area where the case sensitivity comes back again, when searching through those tables).

**Paul Morel**:

No simple way to perform upsert like actions in Postgres.  MySQL has a handy way to performing updates inline when key violations are detected without having to write a function to do so.

**Mike Bayer**:

That is true, PG is really lagging on supporting the SQL standard `MERGE`.  Then again so is MySQL which has it's own homegrown partially-compatible version of `MERGE`.

**Paul Morel**:

`UPDATE` queries using `INNER JOINs` don't work in Postgres.  There is a new syntax for joined table updates using the `UPDATE ... SET ... FROM ... WHERE` rather than `UPDATE ... INNER JOIN ... SET ... WHERE`.  Note the change in position of the `FROM` and `INNER JOIN` so no quick search and replace.  The `FROM` also takes no join conditions directly so they all need to get moved to the `WHERE`.

**Mike Bayer**:

This is true, and SQLAlchemy has support for `UPDATE ... FROM`.  But to refer to the Oracle background, those of us coming from Oracle just use standard SQL correlated criteria in the `WHERE` clause, which is what I usually do with `UPDATE`.

**Paul Morel**:

`INSERT IGNORE` is not available Postgres.  Sure they have a way to do it but it, again, requires writing yet another specialty function.  When we strive to not put too much logic in the database, writing a function is moving away from that goal.  There are a lot of pronouncements why `IGNORE` is a bad idea but there are some current use cases we have that absolutely make `IGNORE` a far more efficient way to import like data into tables.

**Mike Bayer**:

> `INSERT IGNORE` is not available Postgres.

IMHO this is one of MySQL's crazy hacky keywords that people shouldn't be using

> Sure they have a way to do it but it, again, requires writing yet another specialty function.  When we strive to not put too much logic in the database, writing a function is moving away from that goal.  There are a lot of pronouncements why IGNORE is a bad idea but there are some current use cases we have that absolutely make IGNORE a far more efficient way to import like data into tables.

Sure, if your codebase is based on that, and you really need to maintain those semantics, write a stored procedure, yup.

**Paul Morel**:

`GROUP BY` in Postgres follows the SQL standard requiring all non-suummary fields to appear in the `GROUP` BY clause.  MySQL allows for some laziness here where you don't need to list all the fields unless you feel like it.  So, all the `GROUP BY` clauses had to be revisited and updated in many cases to add missing fields.

**Mike Bayer**:

Right, this is another MySQL behavior (apparently SQLite does it too) that I'm pretty strongly against, as it produces random results in many situations. I'd recommend strongly against adding large lists of columns to the `GROUP BY`, as this is not how `GROUP BY` is meant to be used and it will lead to inefficient queries - you should only `GROUP BY` the thing that actually needs to be grouped, in a subquery.  A great article on this technique is here: [http://weblogs.sqlteam.com/jeffs/archive/2005/12/14/8546.aspx](http://weblogs.sqlteam.com/jeffs/archive/2005/12/14/8546.aspx).

**Paul Morel**:

Postgres treats dates as dates and does not accept invalid dates.  MySQL stores bogus dates so during the data migration several errors occurred and cleaning of data was required.

**Mike Bayer**:

Very true!

**Paul Morel**:

There were also a lot of other little things that Postgres does right and MySQL doesn't.  That translates into a lot of little fixes to make syntax "right".

All in all, I think we will be happier with Postgres but it was not a slam dunk converting despite extensive use of SQLAlchemy, which I thought would make the transition naively transparent except for the hand written queries.

We still need to run the performance testing to determine if we get any better performance out of Postgres for our analytics.

*A final note from Rob Martin / @version2beta*:

I'd like to thank both Paul Morel and Mike Bayer for allowing me to document their conversation here. I've changed almost nothing from the emails each provided me, with the exception of making some characters capitalized and adding some puctuation marks.

I fully expect this discussion will be valuable to other developers migrating from MySQL to PostgreSQL. If you should use this article and wish to add to the thoughts, please leave a comment below.

[^mikebayer]: [Mike Bayer][mikebayer] ([@zzzeek][zzzeek] on Twitter) is the author of [SQLAlchemy][], [Alembic][], [Mako][], and other Python tools.

[mikebayer]: http://techspot.zzzeek.org/ "Mike Bayer's blog"

[zzzeek]: https://twitter.com/zzzeek "Mike Bayer on Twitter"

[SQLAlchemy]: http://www.sqlalchemy.org/ "The Python SQL Toolkit and Object Relational Mapper"

[Alembic]: https://alembic.readthedocs.org/en/latest/front.html "Alembic provides SQL migrations and rollbacks, and works with SQLAlchemy"

[Mako]: http://www.makotemplates.org/ "Python templates without XML"
