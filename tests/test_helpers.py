import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.test.simple import DjangoTestSuiteRunner

from changeless.test.myapp.models import Library, Book, Address

def load_fixtures():
    the_place_to_be = Address.objects.create(street_address="THE place")

    our_library = Library.objects.create(name="our library", address=the_place_to_be)

    reader1 = User.objects.create_user(
            'me',
            'me@aol.com',
            'johnpassword')
    reader2 = User.objects.create_user(
            'you',
            'you@gmail.com',
            'johnpassword')
    john = User.objects.create_user(
            'john',
            'lennon@thebeatles.com',
            'johnpassword')

    jacob = User.objects.create_user(
            'jacob',
            'lennon@thebeatles.com',
            'johnpassword')

    jingleheimer = User.objects.create_user(
            'schmidt',
            'not@thebeatles.com',
            'johnpassword')

    a_tail = Book.objects.create(
            title="A Tale of Two Cities",
            author=john,
            location=our_library)

    a_tail.readers.add(reader1)
    a_tail.readers.add(reader2)

    a_tail.save()

    Book.objects.create(
            title="A Tale of One Cities",
            author=john,
            location=our_library)

    Book.objects.create(
            title="A Tale of no Cities",
            author=jingleheimer,
            location=our_library)
