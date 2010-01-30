"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    def check_response_code(self, url, code):
        """
        Check the url to ensure it returns the proper response code
        """
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, code)

    def testContent(self):
        """
        test Content object
        """
        c = Content()
        c.name = "name"
        c.title = "title"
        c.header = "header"
        c.body = "body"
        c.save()

        p = Content.objects.get()
        self.failUnlessEqual(c.name, p.name)
        self.failUnlessEqual(c.title, p.title)
        self.failUnlessEqual(c.header, p.header)
        self.failUnlessEqual(c.body, p.body)
        self.failUnlessEqual(str(p), "name")
