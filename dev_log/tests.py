from django.test import TestCase
from django.core.urlresolvers import reverse

import datetime

from models import *

class SimpleTest(TestCase):

    def get_view(self, url):
        return self.client.get(reverse("dev_log.views." + url))

    # def post_view(self, url, post_data):
        # return self.client.post(reverse("dev_log.views." + url), post_data)

    def test_model_LogEntry(self):
        le = LogEntry()
        le.commit = "7914202e8548bd25854fd69ec653b5798b15de7f"
        le.author = "testuser"
        le.description = "Added test commit for project_showcase"
        le.datetime = datetime.datetime.now()
        le.save()
        le2 = LogEntry.objects.get(commit="7914202e8548bd25854fd69ec653b5798b15de7f")
        self.assertEqual(le.author, le2.author)
        self.assertEqual(le.description, le2.description)
        self.assertEqual(le.datetime.year, le2.datetime.year)
        self.assertEqual(str(le), le2.description)

    def test_view_index(self):
        """
        Tests the index view
        """
        self.assertContains(self.get_view('index'), "")
