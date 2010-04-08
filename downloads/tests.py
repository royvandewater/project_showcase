import django
from django.core.urlresolvers import reverse
from django.test import TestCase

import datetime

from models import *

class DownloadsTest(TestCase):
    fixtures = ['downloads','main']

    def get_view(self, url, get_params=None):
        return self.client.get(reverse("downloads.views." + url, kwargs=get_params))

    def test_model_release(self):
        rel = Release()
        rel.version = "v0.3b"
        rel.release_date = datetime.datetime(2010, 1, 1)
        rel.change_log = "Fixed some stuff"
        rel.file.name = "this/test"
        rel.display_name = None
        rel.save()
        rel2 = Release.objects.get(version="v0.3b")
        self.failUnlessEqual(rel2.version, "v0.3b")
        self.failUnlessEqual(rel2.release_date.year, 2010)
        self.failUnlessEqual(rel2.change_log, "Fixed some stuff")
        self.failUnlessEqual(str(rel2), "v0.3b")
        self.failUnlessEqual(rel2.filename(), "test")
        rel3 = Release()
        rel3.version = "v0.3b"
        rel3.release_date = datetime.datetime.now()
        self.failUnlessRaises(django.db.IntegrityError, rel3.save)
        rel.display_name = "Test display name"
        rel.save()
        rel2 = Release.objects.get(version="v0.3b")
        self.failUnlessEqual(rel2.filename(), "Test display name")

    def test_view_index(self):
        """
        Tests that the main view returns 200
        """
        self.assertContains(self.get_view('index'), "<h1>Downloads</h1>")

    def test_view_show(self):
        """
        Tests that the past release view returns 200
        """
        self.assertContains(self.get_view('show', {'release':'v0.5'}), "<h2>v0.5</h2>")
        self.assertContains(self.get_view('show', {'release':'unstable'}), "<h2>unstable</h2>")

    def test_view_download(self):
        self.assertEqual(self.client.get(reverse('downloads.views.download',kwargs={'file_id':1})).status_code, 200)
