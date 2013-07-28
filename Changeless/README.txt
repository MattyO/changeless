==========
Changeless
==========
Changeless is a set of helpful functions and objects to help convert your data into a set stateless and / immutable data objects.

Types
-----
    from changeless.types import FancyHash, FancyModel, ImmutableHash, ImmutableModel

Fancy Types mearly takes a dict object and replaces the dereferencing operator ([]) with the dot operator
Model Types take a django orm QueueSet and converts to a comperable api.  This uses a Fancy types as a base after converting the QuerySet to a dict.  foreign key and many to many relationships are converted to nested dicts and lists of dicts so getting the models and orm objects operate in very simmular ways.  

* FancyHash(a_dictonary)
* FancyModel(a_model, depth=1)

* ImmutableHash(a_dictonary)
* ImmutableModel(a_model, depth=1)

Just pass the correct object into the type constructor to convert your data.


Decorators
----------
::

    from changeless.decorators import fancy_list

    @fancy_list
    def get_books():
        return Book.objects.all()

Place the following decorators on funcations that return a django orm QueueSet to convert it to the correct data object.  Decorators are the prefered way to use the changeless library.  Using the decorators premote readabilty by keeping the conversion away from orm call as well as providing an easy to way to turn the changeless conversion on and off.  
The following are the gernators that are avalible.  
* fancy_list
* fancy_gen
* immutable_list
* immutable_gen

Functions
----------
I've found the following functions useful.

fuzzyEquals
^^^^^^^^^^^
::

    from changeless.compare import fuzzyEquals

    i_obj = FancyHash({"name":'test name', 
                       'sub_dict':{'name':'sub name', 'attrib':'sub attr value'}
                      })
    second_i_obj = FancyHash({"name":'test name', 
                              'sub_dict':{'name':'sub name', 'attrib':'sub attr value' }})
    self.assertTrue( fuzzyEquals(
         i_obj,
         second_i_obj ))

fuzzyEquals will find if the attributes that the models have in common are equal.  This also inspects nested relationships for shared attributes.

to_dict
^^^^^^^

::

    from changeless.methods import to_dict

to_dict is the reverse conversion from a base fancy_object to its dictonary representation.

