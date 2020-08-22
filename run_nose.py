import os
import nose
import logging

logging.basicConfig(filename="test_log.txt", level=logging.DEBUG)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


os.chdir(os.path.abspath(os.path.dirname(__file__)))

nose.main()

