"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

import django
from django.test import TestCase

import datetime

from models import *

class SimpleTest(TestCase):
    fixtures = ['testdata']
    def check_response_code(self, url, code):
        """
        Check the url to ensure it returns the proper response code
        """
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, code)

    def test_model_release(self):
        rel = Release()
        rel.version = "0.3b"
        rel.release_date = datetime.datetime(2010, 1, 1)
        rel.change_log = "Fixed some stuff"
        rel.save()
        rel2 = Release.objects.get(version="0.3b")
        self.failUnlessEqual(rel2.version, "0.3b")
        self.failUnlessEqual(rel2.release_date.year, 2010)
        self.failUnlessEqual(rel2.change_log, "Fixed some stuff")
        self.failUnlessEqual(str(rel2), "v0.3b")
        rel3 = Release()
        rel3.version = "0.3b"
        rel3.release_date = datetime.datetime.now()
        self.failUnlessRaises(django.db.IntegrityError, rel3.save)

    def test_view_main(self):
        """
        Tests that the main view returns 200
        """
        self.check_response_code("/downloads/", 200)
