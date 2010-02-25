from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    fixtures = ['testdata']

    def testContent(self):
        """
        test Content object
        """
        c = Content()
        c.name = "name"
        c.title = "title"
        c.header = "header"
        c.body = "body"
        c.save()

        p = Content.objects.get(name=c.name)
        self.failUnlessEqual(c.name, p.name)
        self.failUnlessEqual(c.title, p.title)
        self.failUnlessEqual(c.header, p.header)
        self.failUnlessEqual(c.body, p.body)
        self.failUnlessEqual(str(p), "name")

    def testSetting(self):
        """
        tests the user settings object
        """
        s = Setting()
        s.name = "new"
        s.git_key = "4360e8bc7af4ab553732573a176e4e8d"
        s.active = True
        s.save()
        s2 = Setting.objects.get(active=True)
        self.failUnlessEqual(s.name, s2.name)
        self.failUnlessEqual(s.git_key, s2.git_key)
        self.failUnlessEqual(str(s2), s2.name)
