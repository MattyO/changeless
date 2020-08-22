import unittest
import json
import datetime
import types
import os

from changeless.types import FancyHash
from changeless.methods import to_json, to_dict
from changeless.decorators import fancy_gen

from changeless.test.myapp.models import Library, Book, Address

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from test_helpers import load_fixtures
from django.test.simple import DjangoTestSuiteRunner

class TestConverters(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        test_runner = DjangoTestSuiteRunner(interactive=False, verbosity=1)
        test_db = test_runner.setup_databases()
        load_fixtures()


    def test_to_dict(self):
        test_object = FancyHash({"name":"test_name"})
        back_to_dict = to_dict(test_object)

        self.assertEqual( back_to_dict['name'], "test_name")

    def test_to_json(self):
        test_object = FancyHash({"name":"test_name"})
        test_json = to_json(test_object) 
        back_to_dict = json.loads(test_json)


        self.assertEqual( back_to_dict['name'], "test_name")

    def test_to_json_with_nested_attribute(self):
        test_object = FancyHash({"name":"test_name", "attribute":{"attr":"test_attr"}})
        test_json = to_json(test_object) 
        back_to_dict = json.loads(test_json)


        self.assertEqual( back_to_dict['attribute']['attr'], "test_attr")


    def test_to_json_with_nested_dict(self):
        test_object = FancyHash({"name":"test_name", "attribute":{"attr":"test_attr"}})
        test_json = to_json(test_object) 
        back_to_dict = json.loads(test_json)

        self.assertEqual( back_to_dict['attribute']['attr'], "test_attr")

    def test_to_json_with_list(self):
        test_fancy_list = [ 
                FancyHash({"name":"test_name", "thing":"value"}), 
                FancyHash({"name":"test_name2", "thing":"value2"}), 
                ]

        test_json = to_json(test_fancy_list)
        back_to_list = json.loads(test_json)
        self.assertEqual(back_to_list[0]['name'], "test_name")

    def test_to_json_converts_datetime(self):
        test_object = FancyHash({"name":"test", "time":datetime.datetime.now()})
        test_json = to_json(test_object) 
        back_to_dict = json.loads(test_json)

        self.assertIsInstance(back_to_dict['time'], types.UnicodeType)

    def test_to_json_converts_datetime_in_list(self):
        test_object = [FancyHash({"name":"test", "time":datetime.datetime.now()})]
        test_json = to_json(test_object) 
        back_to_dict = json.loads(test_json)

        self.assertIsInstance(back_to_dict[0]['time'], types.UnicodeType)

    def test_to_json_should_convert_datetimes_in_lists(self):
        test_object = [FancyHash({"name":"test", "times":[{"the_time":datetime.datetime.now()}] })]
        test_json = to_json(test_object) 
        back_to_dict = json.loads(test_json)

        self.assertIsInstance(back_to_dict[0]['times'][0]['the_time'], types.UnicodeType)

    def test_to_dict_should_convert_generator(self):
        @fancy_gen
        def get_all_books():
            return Book.objects.filter(title="A Tale of Two Cities")

        book_gen = get_all_books()
        list_of_books_dicts = to_dict(book_gen)
        self.assertEqual(list_of_books_dicts[0]['title'], "A Tale of Two Cities")

    def test_to_json_should_convert_generator(self):
        @fancy_gen
        def get_all_books():
            return Book.objects.filter(title="A Tale of Two Cities")

        book_gen = get_all_books()
        test_json = to_json(book_gen) 
        back_to_dict = json.loads(test_json)
        self.assertEqual(back_to_dict[0]['title'], "A Tale of Two Cities")

