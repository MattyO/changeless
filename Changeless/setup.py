from distutils.core import setup

setup(
    name='changeless',
    version='0.1.0',
    author='Matt ODonnell',
    author_email='odonnell004@gmail.com',
    packages=['changeless', 'changeless.test'],
    url='http://pypi.python.org/pypi/Changeless/',
    license='LICENSE.txt',
    description='Making Immutable and stateless data structures',
    long_description=open('README.txt').read(),
    install_requires=[],
)
