from models import *

from django.test import TestCase

class SimpleTest(TestCase):
    def check_response_code(self, url, code):
        """
        Check the url to ensure it returns the proper response code
        """
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, code)

    def test_model_screenshot(self):
        """
        Tests all methods of the screenshot model
        """
        shot = Screenshot()
        shot.title = "title"
        shot.version = 2.0
        shot.save()
        shot2 = Screenshot.objects.get(title="title")
        self.failUnlessEqual(shot2.title, "title")
        self.failUnlessEqual(shot2.version, 2.0)
        self.failUnlessEqual(str(shot2), "title")

    def test_view_screenshots(self):
        """
        Tests that the screenshots view returns code 200
        """
        self.check_response_code("/screenshots/", 200)
