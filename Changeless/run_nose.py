import os
import nose
import logging

logging.basicConfig(filename="fileinfo", level=logging.DEBUG)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

nose.main()

