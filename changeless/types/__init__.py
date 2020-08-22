from immutable import ImmutableHash, ImmutableModel
from fancy import FancyHash, FancyModel
from conversion_helpers import model_to_dict, dict_to_base_type

def create_fancy_model(django_model, depth=1):
    #temp_dict = model_to_dict(django_model, depth)
    #base_type_dict = dict_to_base_type(temp_dict, FancyModel)

    #return FancyModel(temp_dict)
    return FancyModel(django_model, depth)

def create_immutable_model(django_model, depth=1):
    #temp_dict = model_to_dict(django_model, depth)
    #base_type_dict = dict_to_base_type(temp_dict, ImmutableModel)

    #return ImmutableModel(temp_dict)
    return ImmutableModel(django_model, depth)

