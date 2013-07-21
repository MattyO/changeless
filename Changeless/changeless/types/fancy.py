from conversion_helpers import model_to_dict, dict_to_base_type, base_converter
from django.db.models.fields.related import ForeignKey, ManyToManyField

class BaseFancy(object):
    def __init__(self, a_dict):
        self.__dict__ = dict_to_base_type(a_dict, self)
        #self.__dict__ = dict_to_base_type(a_dict, self, base_converter)

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

class FancyModel(BaseFancy):
    def __init__(self, django_model, depth=1):
        temp_dict = {}

        for field in django_model._meta.local_fields:
            field_value = getattr(django_model, field.name)

            if isinstance(field, ForeignKey) and field_value is not None:
                if depth > 0:
                    temp_dict[field.name] = self.__class__(field_value, depth - 1)
            else:
                temp_dict[field.name] = field_value

        if depth > 0:
            for field in django_model._meta.local_many_to_many:
                field_list = []
                for m2m_item in getattr(django_model, field.name).all():
                    field_list.append(self.__class__(m2m_item, depth -1))
                temp_dict[field.name] = field_list

        self.__dict__.update(temp_dict)


    #def __init__(self, a_dict):
    #    self.__dict__ = dict_to_base_type(a_dict, self)
    #def __init__(self, convert_object):
    #    super(FancyModel, self).__init__(convert_object)
    #    temp_dict = model_to_dict(django_model, depth)
    #    base_type_dict = dict_to_base_type(temp_dict, FanyModel)
    #    print base_type_dict
    #    self.__dict__ = base_type_dict
