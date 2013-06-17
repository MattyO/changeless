from conversion_helpers import model_to_dict, dict_to_base_type

class BaseFancy():
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
    def __init__(self, django_model, depth=1):
        super().__init__(model_to_dict(django_model, depth))



