from types.immutable import ImmutableModel
from types.fancy import FancyHash

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
        r_immutable_list.append(convert_immutables(immutable_obj))
    return r_immutable_list

'''convert all nested immutables into dict.  use im comparison, or kept public for you in cases of pretty printing'''
def to_dict(obj):
    new_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, BaseFancy) :
            new_dict[key] = convert_immutables(value)
        elif isinstance(value, list):
            new_dict[key] = _convert_list_of_fancy_hashes(value)
        else:
            new_dict[key] = value

    return new_dict

'''merges object's dict with one given.   cheaters way out of funcational style'''
'''only works on first level of keys should change'''
def change(obj, new_dict):
    temp_dict = obj.__dict__
    for key,value in new_dict.items():
        temp_dict[key] = value

    return create(temp_dict)

