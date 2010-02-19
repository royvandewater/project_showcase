from django.test import TestCase
from models import *

class SimpleTest(TestCase):

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

        p = Content.objects.get()
        self.failUnlessEqual(c.name, p.name)
        self.failUnlessEqual(c.title, p.title)
        self.failUnlessEqual(c.header, p.header)
        self.failUnlessEqual(c.body, p.body)
        self.failUnlessEqual(str(p), "name")
