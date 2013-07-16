from django.core.management import call_command
import logging


def reset_db(original_functional):
    def new_function(*args, **kwargs):
        call_command('flush',**{'interactive':False})
        original_functional(*args, **kwargs)
    return new_function()
