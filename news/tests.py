"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *

import datetime

class SimpleTest(TestCase):
    fixtures = ['bootstrap']

    def check_response_code(self, url, code):
        """
        Check the url to ensure it returns the proper response code
        """
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, code)

    # models

    def test_model_article(self):
        """
        Tests all methods of the article model (except tags, they get tested in
        their own function
        """
        art1 = Article()
        art1.creation_date = datetime.datetime.now()
        art1.publish_date = datetime.datetime.now()
        art1.title = "test"
        art1.body = "body"
        art1.save()

        art2 = Article.objects.get()
        self.failUnlessEqual(art1, art2)
        self.failUnlessEqual(art1.creation_date.second, art2.creation_date.second)
        self.failUnlessEqual(art1.publish_date.second, art2.publish_date.second)
        self.failUnlessEqual(art2.title, "test")
        self.failUnlessEqual(art2.body, "body")
        art1.delete()

    def test_model_tag(self):
        """
        Tests all methods of the tag model
        """
        tag1 = Tag()
        tag1.name = "test"
        tag1.save()
        tag2 = Tag.objects.get()
        self.failUnlessEqual(tag1, tag2) 
        self.failUnlessEqual(tag2.name, "test") 

    def test_model_relationship_article_tag(self):
        art1 = Article()
        art1.creation_date = datetime.datetime.now()
        art1.publish_date = datetime.datetime.now()
        art1.title = "test"
        art1.body = "body"
        tag1 = Tag()
        tag1.name = "tag1"
        tag1.save()
        tag2 = Tag()
        tag2.name = "tag2"
        tag2.save()
        art1.save()
        art1.tags.add(tag1, tag2)
        art1.save()
        tags = Article.objects.get().tags.all()
        self.failUnlessEqual(tags[0].name, "tag1")
        self.failUnlessEqual(tags[1].name, "tag2")

    # views
    def test_view_news(self):
        """
        Tests that the news view returns code 200
        """
        self.check_response_code("/", 200)
