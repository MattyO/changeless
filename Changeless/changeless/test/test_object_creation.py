from changeless.types import ImmutableHash, ImmutableModel, FancyHash, FancyModel

'''imports used for testing'''
import unittest
import os
from changeless.types.immutable import BaseImmutable
from changeless.types.fancy import BaseFancy
import changeless.types as types

'''for django model conversion testing'''
from changeless.test.decorators import reset_db

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

print "loading testing fill"
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.test.simple import DjangoTestSuiteRunner

from changeless.test.myapp.models import Library, Book, Address

from test_helpers import load_fixtures

class TestFancy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_runner = DjangoTestSuiteRunner(interactive=False, verbosity=1)
        test_db = test_runner.setup_databases()
        load_fixtures()

    def test_fancy_hash_is_fancy_type(self):
        obj = FancyHash({'name': 'test_obj', 'attr1':'attr1_value'})

        self.assertIsInstance(obj, BaseFancy)
        self.assertIsInstance(obj, FancyHash)

    #@reset_db
    def test_fancy_model_is_fancy_type(self):
        obj_model = User.objects.get(username="me")

        print "username in fancy check"
        print obj_model.username

        obj = types.create_fancy_model(obj_model)

        self.assertIsInstance(obj, BaseFancy)
        self.assertIsInstance(obj, FancyModel)

    def test_converts_attributes(self):
        my_instance = FancyHash({"thing_one":"value one", "thing_two":"value two"})

        self.assertEqual(my_instance.thing_one, "value one")
        self.assertEqual(my_instance.thing_two, "value two")

    def test_converts_nested_attribute(self):
        my_instance = FancyHash({"thing_one":"value one", "thing_two":{"name":"thing_two"}})

        self.assertEqual(my_instance.thing_two.name, "thing_two")

    def test_converts_lists(self):
        my_instance = FancyHash({"thing_one":"value one", "a_list":[{"name":"thing_three"},{"name": "thing_four"} ]} )

        self.assertEqual(my_instance.a_list[0].name, "thing_three")
        self.assertEqual(my_instance.a_list[1].name, "thing_four")

    def test_nested_dicts(self):
        my_instance = FancyHash({"thing_one":{"name":"one", "attributes":{"test_attr":"two"}}})
        self.assertEqual(my_instance.thing_one.name, "one")
        self.assertEqual(my_instance.thing_one.attributes.test_attr, "two")

    def test_fancy_model_base_attributes_are_properites(self):
        fancy_model = types.create_fancy_model(User.objects.get(username="me"))
        self.assertEqual(fancy_model.username, "me")
        self.assertEqual(fancy_model.email, "me@aol.com")

    def test_fancy_model_finds_basic_relationship(self):
        fancy_model = types.create_fancy_model(Book.objects.get(title="A Tale of Two Cities"))

        self.assertEqual(fancy_model.author.username, "john")
        self.assertEqual(fancy_model.author.email, "lennon@thebeatles.com")


    def test_fancy_model_default_is_one_relationship_level_deep(self):
        fancy_model = types.create_fancy_model(Book.objects.get(title="A Tale of Two Cities"))

        with self.assertRaises(AttributeError):
            address = fancy_model.location.address

    def test_fancy_model_level_two_attributes(self):
        fancy_model = types.create_fancy_model(Book.objects.get(title="A Tale of Two Cities"), depth=2)

        self.assertEqual(fancy_model.location.address.street_address, "THE place")

    def test_fancy_model_many_to_many_relationships_is_list(self):
        fancy_model = types.create_fancy_model(Book.objects.get(title="A Tale of Two Cities"))

        self.assertIsInstance(fancy_model.readers, list)

    def test_fancy_model_many_to_many_relationships_is_list_with_correct_readers(self):
        fancy_model = types.create_fancy_model(Book.objects.get(title="A Tale of Two Cities"))

        self.assertEqual(len(fancy_model.readers), 2)

class TestImmutable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        test_runner = DjangoTestSuiteRunner(interactive=False, verbosity=1)
        test_db = test_runner.setup_databases()
        load_fixtures()

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
    def test_immutable_model_is_immutable_type(self):
        obj_model = User.objects.get(username="me")

        obj = types.create_immutable_model(obj_model)

        self.assertIsInstance(obj, ImmutableModel)

    def test_immutable_model_base_attributes_are_properites(self):
        fancy_model = ImmutableModel(User.objects.get(username="me"))

        self.assertEqual(fancy_model.username, "me")
        self.assertEqual(fancy_model.email, "me@aol.com")

    def test_immutable_model_finds_basic_relationship(self):
        fancy_model = ImmutableModel(Book.objects.get(title="A Tale of Two Cities"))

        self.assertEqual(fancy_model.author.username, "john")
        self.assertEqual(fancy_model.author.email, "lennon@thebeatles.com")


    def test_immutable_model_default_is_one_relationship_level_deep(self):
        fancy_model = ImmutableModel(Book.objects.get(title="A Tale of Two Cities"))

        with self.assertRaises(AttributeError):
            address = fancy_model.location.address

    def test_immutable_model_level_two_attributes(self):
        fancy_model = ImmutableModel(Book.objects.get(title="A Tale of Two Cities"), depth=2)

        self.assertEqual(fancy_model.location.address.street_address, "THE place")

    def test_immutable_model_many_to_many_relationships_is_list(self):
        fancy_model = ImmutableModel(Book.objects.get(title="A Tale of Two Cities"))

        self.assertIsInstance(fancy_model.readers, list)

    def test_immutable_model_many_to_many_relationships_is_list_with_correct_readers(self):
        immutable_model = ImmutableModel(Book.objects.get(title="A Tale of Two Cities"))

        self.assertEqual(len(immutable_model .readers), 2)



