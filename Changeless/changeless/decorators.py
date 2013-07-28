from changeless.types import create_fancy_model, create_immutable_model

def fancy_list(db_function):
    def create_fancy():
        return lambda: [ create_fancy_model(db_entry) for db_entry in db_function() ]
    return create_fancy()

def immutable_list(db_function):
    def create_immutable():
        return lambda: [ create_immutable_model(db_entry) for db_entry in db_function() ]
    return create_immutable()

def fancy_gen(db_function):
    def create_fancy():
        return lambda: _fancy_gen( db_function() )

    return create_fancy()

def immutable_gen(db_function):
    def create_immutable():
        return lambda: _immutable_gen( db_function() )

    return create_immutable()

def _immutable_gen(query_set):
    for db_entry in query_set:
        yield create_immutable_model(db_entry)

def _fancy_gen(query_set):
    for db_entry in query_set:
        yield create_fancy_model(db_entry)

