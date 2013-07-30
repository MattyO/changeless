from changeless.compare import fuzzyEquals
from changeless.types import FancyHash, FancyModel

import unittest
import os
from test_helpers import load_fixtures

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.test.simple import DjangoTestSuiteRunner

class ComparablesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        test_runner = DjangoTestSuiteRunner(interactive=False, verbosity=1)
        test_db = test_runner.setup_databases()
        load_fixtures()


    def test_fuzzy_equals_with_model(self):
        user = User.objects.get(username='me')

        from_model = FancyModel(user)
        from_create_user = FancyHash( {'username':'me', 'email':'me@aol.com'})

        self.assertTrue(fuzzyEquals(from_create_user, from_model))


    def test_fuzzy_equal_with_nested_converted_like_immutable(self):
        i_obj = FancyHash({"name":'test name', 'sub_dict':{'name':'sub name', 'attrib':'sub attr value'}})
        second_i_obj = FancyHash({"name":'test name', 'sub_dict':{'name':'sub name', 'attrib':'sub attr value' }})
        self.assertTrue( fuzzyEquals(
                i_obj,
                second_i_obj ))

    def test_fuzzy_equal_with_nested_disjoined_converted_like_immutable(self):
        i_obj = FancyHash({"name":'test name', 'sub_dict':{'name':'sub name', 'attrib':'sub attr value'}})
        second_i_obj = FancyHash({"name":'test name', 'sub_dict':{'name':'sub name', 'attrib':'sub attr value', 'disjoined':"test value" }})
        self.assertTrue( fuzzyEquals(
                i_obj,
                second_i_obj ))

    def test_fuzzy_equal_create_with_converted_m2m_like_immutable(self):
        obj_with_relationship = FancyHash({"relationship":[{"attribute":"testValue"}]})
        obj_with_relationship2 = FancyHash({"relationship":[{"attribute":"testValue"}]})
        self.assertTrue(fuzzyEquals(
            obj_with_relationship,
            obj_with_relationship2))

    def test_fuzzy_equal_with_many_to_many_is_false_with_empty_list(self):
        obj_empty = FancyHash({"relationship":[]})
        obj_with_stuff = FancyHash({"relationship":[{"attribute":"testValue"}]})
        self.assertFalse(fuzzyEquals(
                obj_empty,
                obj_with_stuff ))

    def test_fuzzy_equal_with_many_to_many_is_false_with_value(self):
        obj_empty = FancyHash({"relationship":[{"attribute":"testValue not equal"}]})
        obj_with_stuff = FancyHash({"relationship":[{"attribute":"testValue"}]})
        self.assertFalse(fuzzyEquals(
                obj_empty,
                obj_with_stuff ))

    def test_fuzzy_equal_with_many_to_many_is_true(self):
        obj_with_stuff = FancyHash({"relationship":[{"attribute":"testValue"}]})
        obj_with_stuff_again = FancyHash({"relationship":[{"attribute":"testValue"}]})
        self.assertTrue(fuzzyEquals(
                obj_with_stuff, 
                obj_with_stuff_again ))
