from django.test import TestCase
from django.core.urlresolvers import reverse
from django.db import IntegrityError

import datetime

from models import *

class SimpleTest(TestCase):
    fixtures = ['testdata']

    def get_view(self, url, get_params=None):
        return self.client.get(reverse("dev_log.views." + url, kwargs=get_params))

    def post_view(self, url, post_data, get_params=None):
        return self.client.post(reverse("dev_log.views." + url, kwargs=get_params), post_data)

    def test_model_commit(self):
        commit = Commit()
        commit.commit = "7914202e8548bd25854fd69ec653b5798b15de7f"
        commit.commit_url = "http://github.com/defunkt/github/commit/41a212ee83ca127e3c8cf465891ab7216a705f59"
        commit.author = "testuser"
        commit.message = "Added test commit for project_showcase"
        commit.datetime = datetime.datetime.now()
        commit.save()
        commit2 = Commit.objects.get(commit="7914202e8548bd25854fd69ec653b5798b15de7f")
        self.assertEqual(commit.commit_url, commit2.commit_url)
        self.assertEqual(commit.author, commit2.author)
        self.assertEqual(commit.message, commit2.message)
        self.assertEqual(commit.datetime.year, commit2.datetime.year)
        self.assertEqual(str(commit), commit2.message)
        # test that duplicate models raise error
        dup = Commit()
        dup.commit = commit.commit
        dup.commit_url = commit.commit_url
        dup.author = commit.author
        dup.message = commit.message
        dup.datetime = commit.datetime
        self.assertRaises(IntegrityError, dup.save)

    def test_view_index(self):
        """
        Tests the index view
        """
        self.assertContains(self.get_view('index'), "<h1>Development Log</h1>")
        self.assertContains(self.get_view('index'), "3a79575d99d7681de6a1b3bc3b9ba8637a45400d")

    def test_view_github(self):
        """
        Tests the github integration
        """
        kwargs = {'git_key': 'fail'}
        self.assertContains(self.get_view('github', kwargs), 'Method must be post')
        self.assertContains(self.post_view('github', {}, kwargs), "Payload not in post data")
        post_data = self.get_payload()
        self.assertContains(self.post_view('github', post_data, kwargs), 'Github key incorrect')
        kwargs = {'git_key': '4360e8bc7af4ab553732573a176e4e8d'}
        self.assertContains(self.post_view('github', post_data, kwargs), 'Success')
        # Check to make sure the git commits were actually stored
        commit = Commit.objects.get(commit="41a212ee83ca127e3c8cf465891ab7216a705f59")
        self.assertEqual(commit.message, "okay i give in")
        self.assertEqual(commit.datetime.year, 2008)
        self.assertEqual(commit.datetime.minute, 57)

    # Put at the end because its so long
    def get_payload(self):
        return { 'payload':"""
{
  "before": "5aef35982fb2d34e9d9d4502f6ede1072793222d",
  "repository": {
    "url": "http://github.com/defunkt/github",
    "name": "github",
    "description": "You're lookin' at it.",
    "watchers": 5,
    "forks": 2,
    "private": 1,
    "owner": {
      "email": "chris@ozmm.org",
      "name": "defunkt"
    }
  },
  "commits": [
    {
      "id": "41a212ee83ca127e3c8cf465891ab7216a705f59",
      "url": "http://github.com/defunkt/github/commit/41a212ee83ca127e3c8cf465891ab7216a705f59",
      "author": {
        "email": "chris@ozmm.org",
        "name": "Chris Wanstrath"
      },
      "message": "okay i give in",
      "timestamp": "2008-02-15T14:57:17-08:00",
      "added": ["filepath.rb"]
    },
    {
      "id": "de8251ff97ee194a289832576287d6f8ad74e3d0",
      "url": "http://github.com/defunkt/github/commit/de8251ff97ee194a289832576287d6f8ad74e3d0",
      "author": {
        "email": "chris@ozmm.org",
        "name": "Chris Wanstrath"
      },
      "message": "update pricing a tad",
      "timestamp": "2008-02-15T14:36:34-08:00"
    },
    {
      "id": "de8251ff97ee194a289832576287d6f8ad74e3d0",
      "url": "http://github.com/defunkt/github/commit/de8251ff97ee194a289832576287d6f8ad74e3d0",
      "author": {
        "email": "chris@ozmm.org",
        "name": "Chris Wanstrath"
      },
      "message": "update pricing a tad",
      "timestamp": "2008-02-15T14:36:34-08:00"
    }
  ],
  "after": "de8251ff97ee194a289832576287d6f8ad74e3d0",
  "ref": "refs/heads/master"
}
""" }
