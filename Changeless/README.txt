Changeless is a set of functions and objects to help convert your data
into a set stateless or immutable data objects.

Types
=====

> from changeless.types import FancyHash, FancyModel, ImmutableHash,
> ImmutableModel

Fancy Types take a dict object and replaces the dereferencing operator
([]) with the dot operator. So the object

> an\_obj= FancyHash({"name":"me"})

will allow us to retrieve the attribute 'name' with

> print "the object's name: " + an\_obj.name \>the object's name: matt

Model Types take a Django ORM QueueSet and converts it to a comparable
api. This uses the Fancy type as a base after converting the QuerySet to
a dict. Foreign keys and many to many relationships are converted to
nested dicts and lists of dicts(respectively) to aid in the objects
behaving as similarly as possible.

Note that Model Types retrieve all of data at once which includes by
default relationships directly adjacent. This might incur more queries
than expected. Choose your data carefully and scale back when necessary.

-   FancyHash(a\_dictonary)
-   FancyModel(a\_model, depth=1)
-   ImmutableHash(a\_dictonary)
-   ImmutableModel(a\_model, depth=1)

Just pass the correct object into the type constructor to convert your
data.

Decorators
==========

> from changeless.decorators import fancy\_list
>
> @fancy\_list def get\_books(): return Book.objects.all()

Place the following decorators before functions that return a Django ORM
QueueSet to convert it to the correct changeless object. Decorators are
the preferred way to use the changeless library. Using the decorators
promote readability by keeping the conversion away from the ORM call, as
well as providing an easy to way to turn the changeless conversion on
and off. Notice that the \_gen decorators will return a generator that
will lazily convert each object in the list. Generators may be more
efficient for long lists.

The following generators are available. \* fancy\_list \* fancy\_gen \*
immutable\_list \* immutable\_gen

Functions
=========

I've found the following functions useful. \#\#\#fuzzyEquals\#\#\# from
changeless.compare import fuzzyEquals

> i\_obj = FancyHash({"name":'test name',
> :   'sub\_dict':{'name':'sub name', 'attrib':'sub attr value'}
>
> > })
>
> second\_i\_obj = FancyHash({"name":'test name',
> :   'sub\_dict':{'name':'sub name', 'attrib':'sub attr value' }})
>
> self.assertTrue( fuzzyEquals(
> :   i\_obj, second\_i\_obj ))
>
fuzzyEquals will find attributes that the changeless objects have in
common and compare only that union. This also inspects nested
relationships for shared attributes. \#\#\#to\_dict\#\#\# from
changeless.methods import to\_dict to\_dict is the reverse conversion
from a base fancy\_object to its dictionary representation.
