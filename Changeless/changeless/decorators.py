def _immutable_gen(query_set):
    for db_entry in query_set:
        yield ImmutableModel(db_entry)

def _fancy_gen(query_set):
    for db_entry in query_set:
        yield FancyModel(db_entry)


def fancy_list(db_function):
    def create_fancy():
        return lambda: [ FancyModel(db_entry) for db_entry in db_function() ]
    return create_fancy()

def immutable_list(db_function):
    def create_immutable():
        return lambda: [ ImmutableModel(db_entry) for db_entry in db_function() ]
    return create_immutable()

def fancy_gen(db_function):
    def create_fancy():
        return lambda: _fancy_gen( db_function() )

    return create_fancy()

def immutable_gen(db_function):
    def create_immutable():
        return lambda: _immutable_gen( db_function() )

    return create_immutable()
