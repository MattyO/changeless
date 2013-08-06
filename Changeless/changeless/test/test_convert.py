import unittest
from changeless.types import FancyHash
from changeless.methods import to_json, to_dict
import json

class TestConverters(unittest.TestCase):

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


