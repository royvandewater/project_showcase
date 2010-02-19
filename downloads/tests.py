import django
from django.core.urlresolvers import reverse
from django.test import TestCase

import datetime

from models import *

class DownloadsTest(TestCase):
    fixtures = ['testdata']

    def url(self, url):
        return self.client.get("/downloads%s" % (url))

    def test_model_release(self):
        rel = Release()
        rel.version = "0.3b"
        rel.release_date = datetime.datetime(2010, 1, 1)
        rel.change_log = "Fixed some stuff"
        rel.file.name = "this/test"
        rel.display_name = None
        rel.save()
        rel2 = Release.objects.get(version="0.3b")
        self.failUnlessEqual(rel2.version, "0.3b")
        self.failUnlessEqual(rel2.release_date.year, 2010)
        self.failUnlessEqual(rel2.change_log, "Fixed some stuff")
        self.failUnlessEqual(str(rel2), "v0.3b")
        self.failUnlessEqual(rel2.filename(), "test")
        rel3 = Release()
        rel3.version = "0.3b"
        rel3.release_date = datetime.datetime.now()
        self.failUnlessRaises(django.db.IntegrityError, rel3.save)
        rel.display_name = "Test display name"
        rel.save()
        rel2 = Release.objects.get(version="0.3b")
        self.failUnlessEqual(rel2.filename(), "Test display name")

    def test_view_main(self):
        """
        Tests that the main view returns 200
        """
        self.assertContains(self.url("/"), "<h1>Downloads</h1>", status_code=200)

    def test_view_past_release(self):
        """
        Tests that the past release view returns 200
        """
        self.assertContains(self.url("/0.50/"), "<h2>v0.5</h2>", status_code=200)

    def test_view_download(self):
        self.assertEqual(self.client.get(reverse('downloads.views.download',kwargs={'file_id':1})).status_code, 200)
