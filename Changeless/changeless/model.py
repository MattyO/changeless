from base import BaseImmutable
from django.db.models.fields.related import ForeignKey, ManyToManyField
class ImmutableModel(BaseImmutable):
    def __init__(self, django_model, depth=1):
        temp_dict = {}
        for field in django_model._meta.local_fields:
            field_value = getattr(django_model, field.name)

            if isinstance(field, ForeignKey) and field_value is not None:
                if depth > 0 or depth == -1 :
                    temp_dict[field.name] = ImmutableModel(field_value, depth - 1)
            else:
                temp_dict[field.name] = field_value

        if depth > 0 or depth == -1:
            for field in django_model._meta.local_many_to_many:
                field_list = []
                for m2m_item in getattr(django_model, field.name).all():
                    field_list.append(ImmutableModel(m2m_item, depth -1))
                temp_dict[field.name] = field_list

        self.__dict__ = temp_dict
