from conversion_helpers import model_to_dict, dict_to_base_type

class BaseFancy(object):
    def __init__(self, a_dict):
        self.__dict__ = dict_to_base_type(a_dict, self)

    def __eq__(self, other):
        if not other.__dict__ == self.__dict__:
            print "this: " + str(self.__dict__)
            print "is not equal to this: " + str(other.__dict__)

        return other.__dict__ == self.__dict__

    def __ne__(self, other):
        return not self.__eq__(other.__dict__)

class FancyHash(BaseFancy):
    pass

class FancyModel(BaseFancy):
    pass
    #def __init__(self, a_dict):
    #    self.__dict__ = dict_to_base_type(a_dict, self)
    #def __init__(self, convert_object):
    #    super(FancyModel, self).__init__(convert_object)
    #    temp_dict = model_to_dict(django_model, depth)
    #    base_type_dict = dict_to_base_type(temp_dict, FanyModel)
    #    print base_type_dict
    #    self.__dict__ = base_type_dict
