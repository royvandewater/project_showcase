from models import *
from helpers import *
import datetime

from django.test import TestCase

class SimpleTest(TestCase):
    fixtures = ['testdata']

    def check_response_code(self, url, code):
        """
        Check the url to ensure it returns the proper response code
        """
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, code)

    def test_model_version(self):
        ver = Version()
        ver.version = "0.2b"
        ver.release_date = datetime.datetime.now()
        ver.save()
        ver2 = Version.objects.get(version="0.2b")
        self.failUnlessEqual(ver2.version, "0.2b")
        self.failUnlessEqual(str(ver2), "v0.2b")
        self.failUnlessEqual(ver2.release_date.year, ver.release_date.year)

    def test_model_screenshot(self):
        """
        Tests all methods of the screenshot model
        """
        ver = Version()
        ver.version = "0.2b"
        ver.release_date = datetime.datetime.now()
        ver.save()
        shot = Screenshot()
        shot.title = "title"
        shot.version = ver
        shot.save()
        shot2 = Screenshot.objects.get(title="title")
        self.failUnlessEqual(shot2.title, "title")
        self.failUnlessEqual(str(shot2), "title")

    def test_model_relationship_screenshot_version(self):
        ver1 = Version()
        ver1.version = "0.2b"
        ver1.release_date = datetime.datetime(2009,12,01)
        ver1.save()
        shot = Screenshot()
        shot.title = "title"
        shot.version = ver1
        shot.save()
        shot2 = Screenshot.objects.get(title="title")
        self.failUnlessEqual(str(shot2.version), "v0.2b")

    def test_view_screenshots(self):
        """
        Tests that the screenshots view returns code 200
        """
        self.check_response_code("/screenshots/", 200)
        self.check_response_code("/screenshots/0.3a/", 200)

