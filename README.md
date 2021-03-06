Changeless is a set of functions and objects to help convert your data into a set stateless or immutable data objects.

Types
-----
    from changeless.types import FancyHash, FancyModel, ImmutableHash, ImmutableModel

Fancy Types take a dict object and replaces the dereferencing operator ([]) with the dot operator.  So the object

     an_obj= FancyHash({"name":"me"}) 

will allow us to retrieve the attribute 'name' with

    print "the object's name: " + an_obj.name
    >the object's name: matt

 
Model Types take a Django ORM QueueSet and converts it to a comparable api.  This uses the Fancy type as a base after converting the QuerySet to a dict.  Foreign keys and many to many relationships are converted to nested dicts and lists of dicts(respectively) to aid in the objects behaving as similarly as possible.  

Note that Model Types retrieve all of data at once which includes by default relationships directly adjacent.  This might incur more queries than expected.  Choose your data carefully and scale back when necessary. 

* FancyHash(a_dictonary)
* FancyModel(a_model, depth=1)
* ImmutableHash(a_dictonary)
* ImmutableModel(a_model, depth=1)

Just pass the correct object into the type constructor to convert your data.
###FancyHash###
    fancy_object = FancyHash({
	    "a_key":"a_value", 
	    "a_relationship":{"a_attribute":"attribute_value"}, 
	    "relationship_list:[{"name:"name_1", "attr_1":"value2"}, {"name:"name_2", "attr_1":"value3"}]
	    })

    fancy_object.a_key
    > a_value

    fancy_object.a_relationship.a_attribute
    >attribute_value

    for a_thing in fancy_object.relationship_list:
        a_thing.name
    >name_1
    >name_2


###FancyModel###
    from django.db import models

    class Poll(models.Model):
        question = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

    class Choice(models.Model):
        poll = models.ForeignKey(Poll)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)

    fancy_choice  = FancyModel(Choice.objects.get(pk=1))
    fancy_choice.votes
    >2
    fancy_choice.poll.question
    >"how great is this?"



Decorators
----------
    from changeless.decorators import fancy_list

    @fancy_list
    def get_choices():
        return Choice.objects.all()

    for choice in get_choices():
        print choice.choice_text

    >"Kind of great"
    >"Sort of great"
    >"Really great"

Place the following decorators before functions that return a Django ORM QueueSet to convert it to the correct changeless object.  Decorators are the preferred way to use the changeless library.  Using the decorators promote readability by keeping the conversion away from the ORM call, as well as providing an easy to way to turn the changeless conversion on and off.  Notice that the _gen decorators will return a generator that will lazily convert each object in the list.  Generators may be more efficient for long lists.

The following generators are available.  
* fancy_list
* fancy_gen
* immutable_list
* immutable_gen

Functions
----------
I've found the following functions useful.
###fuzzyEquals###
    from changeless.compare import fuzzyEquals

    i_obj = FancyHash({"name":'test name', 
                       'sub_dict':{'name':'sub name', 'attrib':'sub attr value'}
                      })
    second_i_obj = FancyHash({"name":'test name', 
                              'sub_dict':{'name':'sub name', 'attrib':'sub attr value' }})
    self.assertTrue( fuzzyEquals(
         i_obj,
         second_i_obj ))

fuzzyEquals will find attributes that the changeless objects have in common and compare only that union.  This also inspects nested relationships for shared attributes.
###to_dict###
    from changeless.methods import to_dict
to_dict is the reverse conversion from a base fancy_object to its dictionary representation.  attributes become keys, relationships become nested dictonaries, many to many relationships become list with dicts


