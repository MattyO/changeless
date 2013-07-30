import unittest
from changeless.types.conversion_helpers import model_to_dict
from django.test.simple import DjangoTestSuiteRunner
from test_helpers import load_fixtures
from changeless.test.myapp.models import Library, Book, Address
import pprint

class TestConverters(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_runner = DjangoTestSuiteRunner(interactive=False, verbosity=1)
        test_db = test_runner.setup_databases()
        load_fixtures()

    #def test_model_to_dict(self):
    #    pp = pprint.PrettyPrinter(indent=4)
    #    model_dict = model_to_dict(Book.objects.get(title="A Tale of Two Cities"))

    #    pp.pprint(model_dict)

    #    self.assertTrue(False)

