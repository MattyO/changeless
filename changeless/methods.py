from changeless.types.immutable import ImmutableModel
from changeless.types.fancy import FancyHash, BaseFancy
from changeless.decorators import fancy_gen
import json
import datetime
import logging

def _generatorType():
    @fancy_gen
    def generator_type_function():
        pass
    generator_obj = generator_type_function()
    return type(generator_obj)

GeneratorType = _generatorType()

'''return dictonary object of object given keys minus ignore keys'''
def _sub_dict(object, keys, ignore=[]):
    return_dict = {}

    for key, value in object.__dict__.items():
        if key in keys and key not in ignore:
            return_dict[key] = value

'''return recursive (dictonaries within dictonaries) union of dictonary object.  object and sec_object must be dicts '''
def _r_sub_dict(object, second_obj):
    #todo: add checking for lists and convert immutable models contained within them.
    return_dict = {}
    for key,value in object.items():
        if key in second_obj.keys():
            if isinstance(value, dict) and isinstance(second_obj[key],dict):
                return_dict[key] = _r_sub_dict(value, second_obj[key])
            else:
                return_dict[key] = value

    return return_dict

def _convert_list_of_fancy_hashes(a_list):
    r_immutable_list = []
    for immutable_obj in a_list:
        r_immutable_list.append(to_dict(immutable_obj))
    return r_immutable_list

'''convert all nested immutables into dict.  use im comparison, or kept public for you in cases of pretty printing'''
def to_dict(obj):
    new_dict = {}
    if isinstance(obj, list) or isinstance(obj, GeneratorType):
        return [ to_dict(dict_obj) for dict_obj in obj ]
    else: 
        for key, value in obj.__dict__.items():
            #logging.debug( type(value)  )
            if isinstance(value, BaseFancy) :
                new_dict[key] = to_dict(value)
            elif isinstance(value, list) or isinstance(value, GeneratorType):
                new_dict[key] = _convert_list_of_fancy_hashes(value)
            else:
                new_dict[key] = value

    return new_dict


def to_json(obj):
    jsonable = None

    if isinstance(obj, list) or isinstance(obj, GeneratorType):
        jsonable = [ _datetimes_to_string(to_dict(changless_obj)) for changless_obj in obj ]
    else: 
        jsonable = _datetimes_to_string(to_dict(obj))

    return json.dumps(jsonable)

def _datetimes_to_string(obj):
    converted = obj
    for key, value in obj.items():
        if isinstance(value, dict):
            converted[key] = _datetimes_to_string(value)
        elif isinstance(value, list) or isinstance(value, GeneratorType):
            converted[key] = [ _datetimes_to_string(dict_obj) for dict_obj in value ]

        elif isinstance(value, datetime.datetime):
            converted[key] = value.isoformat()
            
    return converted 

