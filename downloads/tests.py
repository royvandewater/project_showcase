"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class SimpleTest(TestCase):
    fixtures = ['testdata']
    def check_response_code(self, url, code):
        """
        Check the url to ensure it returns the proper response code
        """
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, code)

    def test_view_main(self):
        """
        Tests that the main view returns 200
        """
        self.check_response_code("/downloads/", 200)
