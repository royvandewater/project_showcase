from django.test import TestCase

import datetime

from models import *
from users.models import ProjectUser

class SimpleTest(TestCase):

    def test_model_status(self):
        """
        Tests the State model
        """
        s = Status()
        s.name = "FakeState"
        s.save()
        q = Status.objects.all()
        s2 = q[q.count() - 1]
        self.assertEqual(s2.name, s.name)
        self.assertEqual(str(s2), s.name)

    def test_model_ticket(self):
        """
        Tests the Ticket model
        """
        t = Ticket()
        t.name = "name"
        s = Status()
        s.name = "FakeState"
        s.save()
        t.status = s
        t.description = "description"
        t.open_date = datetime.datetime(2009, 12, 24)
        t.close_date = datetime.datetime(2010, 01, 29)

        projectUser = ProjectUser()
        projectUser.build_user("testuser","first","last","test@test.com")
        projectUser.save()
        t.creator = projectUser

        t.priority = 3
        t.save()
        t2 = Ticket.objects.get(name="name")
        self.failUnlessEqual(t.name, t2.name)
        self.failUnlessEqual(t.status, t2.status)
        self.failUnlessEqual(t.description, t2.description)
        self.failUnlessEqual(t.open_date.year, t2.open_date.year)
        self.failUnlessEqual(t.close_date.year, t2.close_date.year)
        self.failUnlessEqual(t.creator, t2.creator)
        self.failUnlessEqual(t.priority, t2.priority)
        self.failUnlessEqual(str(t2), t2.name)

    def test_relationship_ticket_commnt(self):
        pass
        # c1 = Comment()
        # c1.author = projectUser
        # c1.message = "First"
        # c1.save()
        # c2 = Comment()
        # c2.author = projectUser
        # c2.message = "Second"
        # c2.save()

        # t.comments = [c1, c2]
        # self.failUnlessEqual(t.comments[0], t2.comments[0])
