"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *
from views import *

import datetime

class SimpleTest(TestCase):
    fixtures = ['testdata']

    def url(self, url):
        return self.client.get("/news%s" % (url))

    # models

    def test_model_article(self):
        """
        Tests all methods of the article model (except tags, they get tested in
        their own function
        """
        art1 = Article()
        art1.publish_date = datetime.datetime.now()
        art1.title = "test"
        art1.body = "body"
        art1.save()

        art2 = Article.objects.get(title="test")
        self.failUnlessEqual(art1, art2)
        self.failUnlessEqual(art1.publish_date.second, art2.publish_date.second)
        self.failUnlessEqual(art2.title, "test")
        self.failUnlessEqual(art2.body, "body")
        self.failUnlessEqual(str(art2), "test")

    def test_model_tag(self):
        """
        Tests all methods of the tag model
        """
        tag1 = Tag()
        tag1.name = "test"
        tag1.save()
        tag2 = Tag.objects.get(name="test")
        self.failUnlessEqual(tag1, tag2) 
        self.failUnlessEqual(tag2.name, "test") 
        self.failUnlessEqual(str(tag2), "test") 

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
        tags = Article.objects.get(title="test").tags.all()
        self.failUnlessEqual(tags[0].name, "tag1")
        self.failUnlessEqual(tags[1].name, "tag2")

    # view helpers
    def test_get_article_dates(self):
        dates = get_article_dates()
        self.failUnlessEqual(dates[2010][0].year, 2010)

    # views
    def test_view_news(self):
        """
        Tests that the news view returns code 200
        """
        self.assertContains( self.url("/"), "<h1>News</h1>", status_code=200)

    def test_view_archive(self):
        """
        Tests that the archive view returns code 200
        """
        self.assertContains( self.url("/archive/2010/01/"), "<h2>January, 2010</h2>", status_code=200)
