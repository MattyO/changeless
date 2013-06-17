def dict_to_base_type(a_dict, base_type):
    converted_dict = {}
    for key, value in a_dict.items():
        if isinstance(value, dict):
            converted_dict[key] = base_type(value)
        elif isinstance(value, list):
            converted_dict[key] = convert_list_of_dict(value, base_type)
        else:
            converted_dict[key] = value

    return converted_dict 

def list_of_dict_to_base_type(the_list_of_dicts, base_type):
    return [ base_type(an_item) for an_item in the_list_of_dicts ]

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
