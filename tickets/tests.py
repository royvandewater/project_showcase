from django.test import TestCase

import datetime

from models import *
from users.models import ProjectUser

class SimpleTest(TestCase):

    def test_model_comment(self):
        """
        Tests the Comment model
        """
        c = Comment()
        author = ProjectUser()
        author.build_user("testuser","first","last","test@test.com")
        author.save()
        c.author = author
        c.message = "Test message"
        c.datetime = datetime.datetime.now()
        c.save()
        c2 = Comment.objects.get(author=author)
        self.assertEqual(c2.message, c.message)
        self.assertEqual(c2.datetime.minute, c.datetime.minute)

    def test_model_ticket(self):
        """
        Tests the Ticket model
        """
        t = Ticket()
        t.name = "name"
        t.status = "status"
        t.description = "description"
        t.open_date = datetime.datetime(2009, 12, 24)
        t.close_date = datetime.datetime(2010, 01, 29)

        projectUser = ProjectUser()
        projectUser.build_user("testuser","first","last","test@test.com")
        t.creator = projectUser

        c1 = Comment()
        c1.author = projectUser
        c1.message = "First"
        c1.save()
        c2 = Comment()
        c2.author = projectUser
        c2.message = "Second"
        c2.save()

        t.comments = [c1, c2]
        t.priority = 3
        t.save()
        t2 = Ticket.objects.get(name="name")
        self.failUnlessEqual(t.name, t2.name)
        self.failUnlessEqual(t.states, t2.states)
        self.failUnlessEqual(t.description, t2.description)
        self.failUnlessEqual(t.open_date.year, t2.open_date.year)
        self.failUnlessEqual(t.close_date.year, t2.close_date.year)
        self.failUnlessEqual(t.creator, t2.creator)
        self.failUnlessEqual(t.comments[0], t2.comments[0])
        self.failUnlessEqual(t.priority, t2.priority)
