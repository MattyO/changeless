from changeless.decorators import fancy_list, immutable_list
from changeless.types import ImmutableHash, ImmutableModel, FancyHash, FancyModel


import unittest
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from test_helpers import load_fixtures
from django.test.simple import DjangoTestSuiteRunner

from changeless.test.myapp.models import Library, Book, Address

class TestDecorators(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_runner = DjangoTestSuiteRunner(interactive=False, verbosity=1)
        test_db = test_runner.setup_databases()
        load_fixtures()

    def test_fancy_list_returns_correct_types(self):
        @fancy_list
        def get_books():
            return Book.objects.all()

        fancy_book_list = get_books()

        self.assertIsInstance(fancy_book_list, list)
        self.assertEqual(len(fancy_book_list) , 3)
        self.assertIsInstance(fancy_book_list[0], FancyModel)

    def test_fancy_list_object_gets_attributes(self):
        @fancy_list
        def get_cities():
            return Book.objects.filter(title="A Tale of Two Cities")

        fancy_book_list = get_cities()
        self.assertEqual(fancy_book_list[0].title , "A Tale of Two Cities")

    def test_immutable_list_returns_correct_types(self):
        @immutable_list
        def get_books():
            return Book.objects.all()

        immutable_book_list = get_books()

        self.assertIsInstance(immutable_book_list, list)
        self.assertEqual(len(immutable_book_list ) , 3)
        self.assertIsInstance(immutable_book_list[0], ImmutableModel)

    def test_immutable_list_object_gets_attributes(self):
        @immutable_list
        def get_cities():
            return Book.objects.filter(title="A Tale of Two Cities")

        immutable_book_list = get_cities()

        self.assertEqual(immutable_book_list[0].title , "A Tale of Two Cities")

