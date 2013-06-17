from changeless.types import ImmutableHash, ImmutableModel, FancyHash, FancyModel

'''imports used for testing'''
import unittest
import os
from decorators import reset_db
from changeless.types.immutable import BaseImmutable
from changeless.types.fancy import BaseFancy

'''for django model conversion testing'''
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.test.simple import DjangoTestSuiteRunner

from myapp.models import Library, Book, Address


class TestImmutable(unittest.TestCase):
    def test_immutable_hash_is_immutable_type(self):
        is_immutable = True;
        obj = ImmutableHash({'name': 'test_obj', 'attr1':'attr1_value'})

        '''checking inheritance'''
        '''and terrible things don't happen during init'''
        self.assertIsInstance(obj, BaseFancy)
        self.assertIsInstance(obj, BaseImmutable)
        self.assertIsInstance(obj, ImmutableHash)

    def test_immutable_hash_is_immutable(self):
        is_immutable = False;
        obj = ImmutableHash({'name': 'test_obj', 'attr1':'attr1_value'})
        with self.assertRaises(Exception) as cm:
            obj.name = "new name"

    #@reset_db
    #def test_immutable_model_is_immutable_type(self):
    #    is_immutable = True;
    #    obj = ImmutableModel({'name': 'test_obj', 'attr1':'attr1_value'})

    #    with self.assertRaises(Exception) as cm:
    #        super(obj).name = "Immutable"
    #    self.assertTrue(is_immutable)

    def test_fancy_hash_is_fancy_type(self):
        obj = FancyHash({'name': 'test_obj', 'attr1':'attr1_value'})

        self.assertIsInstance(obj, BaseFancy)
        self.assertIsInstance(obj, FancyHash)

    def test_fancy_hash_single_attribute(self):
        obj = FancyHash({'name': 'test_obj', 'attr1':'attr1_value'})
        self.assertEqual(obj.name, "test_obj")


    #@reset_db
    #def test_fancy_model_is_fancy_type(self):
    #    is_immutable = True;
    #    obj = ImmutableModel({'name': 'test_obj', 'attr1':'attr1_value'})

    #    with self.assertRaises(Exception) as cm:
    #        super(obj).name = "Immutable"
