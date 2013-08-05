from distutils.core import setup
import os

version_string = '0.1.' + str(os.environ['BUILD_NUMBER'])

setup(
    name='changeless',
    version=version_string,
    author='Matt ODonnell',
    author_email='odonnell004@gmail.com',
    packages=['changeless', 'changeless.test', 'changeless.types'],
    url='http://pypi.python.org/pypi/Changeless/',
    license='LICENSE.txt',
    description='Making Immutable and stateless data structures',
    long_description=open('README.txt').read(),
    install_requires=[],
)
