from fancy import BaseFancy, FancyModel
from conversion_helpers import model_to_dict

class BaseImmutable(BaseFancy):
    def __setattr__(self, name, value):
        if name != "__dict__":
            raise Exception("Immutable Object can not be changed")

class ImmutableHash(BaseImmutable):
    pass

class ImmutableModel(FancyModel):

    def __setattr__(self, name, value):
        if name != "__dict__":
            raise Exception("Immutable Object can not be changed")
    #def __init__(self, converted_object):
    #    super(ImmutableModel, self).__init__(converted_object)
        #self.__dict__ = converted_object
    #def __init__(self, django_model, depth=1):
    #    temp_dict = model_to_dict(django_model, depth)
    #    print temp_dict
    #    self.__dict__ = dict_to_base_type(temp_dict, BaseImmutable)

