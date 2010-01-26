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

    # models
    def test_article_model(self):
        """
        Tests all methods of the article model
        """
        testArticle = Article()
        testArticle.save()
        retrieveArticle = Article.objects.get()
        self.failUnlessEqual(testArticle, retrieveArticle)
        testArticle.delete()

    # views
    def test_news_response(self):
        """
        Tests that the news view returns code 200
        """
        self.check_response_code('/', 200)

