from django.db.models.fields.related import ForeignKey, ManyToManyField

def base_converter(base_type, a_dict):
    return base_type.__class__(a_dict)

def model_converter(base_type, a_model, depth=1):
    temp_dict = model_to_dict(a_model, depth)
    return base_type.__class__(temp_dict)

def convert_list_to(the_list, base_type):
    return [ base_type.__class__(an_item) for an_item in the_list ]


def dict_to_base_type(a_dict, base_type):
    converted_dict = {}
    for key, value in a_dict.items():
        if isinstance(value, dict):
            converted_dict[key] = base_type.__class__(value)
        elif isinstance(value, list):
            converted_dict[key] = convert_list_to(value, base_type)
        else:
            converted_dict[key] = value

    return converted_dict 

#def dict_to_base_type(a_dict, base_type):
#    converted_dict = {}
#    for key, value in a_dict.items():
#        if isinstance(value, dict):
#            converted_dict[key] = base_type(value)
#        elif isinstance(value, list):
#            converted_dict[key] = convert_list_to(value, base_type)
#        else:
#            converted_dict[key] = value
#
#    return converted_dict 


def model_to_dict(django_model, depth=1):

    temp_dict = {}

    for field in django_model._meta.local_fields:
        field_value = getattr(django_model, field.name)

        if isinstance(field, ForeignKey) and field_value is not None:
            if depth > 0:
                temp_dict[field.name] = model_to_dict(field_value, depth - 1)
        else:
            temp_dict[field.name] = field_value

    if depth > 0:
        for field in django_model._meta.local_many_to_many:
            field_list = []
            for m2m_item in getattr(django_model, field.name).all():
                field_list.append(model_to_dict(m2m_item, depth -1))
            temp_dict[field.name] = field_list

    return temp_dict
