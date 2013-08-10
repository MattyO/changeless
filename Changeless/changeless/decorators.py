from changeless.types import FancyModel, ImmutableModel

def fancy_list(*args, **kwargs):
    depth = 1
    if kwargs.has_key('depth'):
        depth = kwargs['depth']

    def wrapped(db_function):
        def create_fancy():
            print "depth is " + str(depth)
            return lambda: [ FancyModel(db_entry, depth) for db_entry in db_function() ]
        return create_fancy()

    if len(args) == 1 and callable(args[0]):
        return wrapped(args[0])
    else:
        return wrapped

def immutable_list(*args, **kwargs):
    depth = 1
    if kwargs.has_key('depth'):
        depth = kwargs['depth']

    def wrapped(db_function):
        def create_immutable():
            return lambda: [ ImmutableModel(db_entry, depth) for db_entry in db_function() ]

        return create_immutable()

    if len(args) == 1 and callable(args[0]):
        return wrapped(args[0])
    else:
        return wrapped

def fancy_gen(*args, **kwargs):
    depth = 1
    if kwargs.has_key('depth'):
        depth = kwargs['depth']

    def wrapped(db_function):

        def create_fancy():
            return lambda: _fancy_gen( db_function(), depth )
        return create_fancy()

    if len(args) == 1 and callable(args[0]):
        return wrapped(args[0])
    else:
        return wrapped


def immutable_gen(*args, **kwargs):
    depth = 1
    if kwargs.has_key('depth'):
        depth = kwargs['depth']

    def wrapped(db_function):
        def create_immutable():
            return lambda: _immutable_gen( db_function(), depth )

        return create_immutable()

    if len(args) == 1 and callable(args[0]):
        return wrapped(args[0])
    else:
        return wrapped

def _immutable_gen(query_set, depth):
    for db_entry in query_set:
        yield FancyModel(db_entry, depth)

def _fancy_gen(query_set, depth):
    for db_entry in query_set:
        yield FancyModel(db_entry, depth)

