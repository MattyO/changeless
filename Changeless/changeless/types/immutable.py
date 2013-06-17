from fancy import BaseFancy
from conversion_helpers import model_to_dict

class BaseImmutable(BaseFancy):
    def __setattr__(self, name, value):
        raise Exception("Immutable Object can not be changed")

class ImmutableHash(BaseImmutable):
    pass

class ImmutableModel(BaseImmutable):
    def __init__(self, django_model, depth=1):
        super().__init__(model_to_dict(django_model, depth))

