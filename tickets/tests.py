from django.test import TestCase
from django.core.urlresolvers import reverse

import datetime

from models import *
from users.models import ProjectUser

class TicketsTest(TestCase):
    fixtures = ['tickets','main','users']

    def get_view(self, url):
        try:
            url.index(".") # Will throw ValueError if contains no .'s
            return self.client.get(reverse(url))
        except ValueError:
            return self.client.get(reverse("tickets.views." + url))

    def post_view(self, url, post_data):
        try:
            url.index(".") # Will throw ValueError if contains no .'s
            return self.client.post(reverse(url), post_data)
        except ValueError:
            return self.client.post(reverse("tickets.views." + url), post_data)

    def log_in(self):
        post_data = {
                'username':'test',
                'password':'password',
                }
        self.post_view("users.views.login", post_data)

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

    def test_model_comment(self):
        """
        Tests the Comment model
        """
        u = ProjectUser.objects.all()[0]
        t = Ticket.objects.all()[0]
        c = Comment()
        c.user = u
        c.message = "Comment message"
        c.ticket = t
        c.save()
        c2 = Comment.objects.get(message="Comment message")
        self.failUnlessEqual(c.message, c2.message)
        self.failUnlessEqual(str(c), u.user.email)


    def test_relationship_ticket_comment(self):
        # Build a user
        projectUser = ProjectUser()
        projectUser.build_user("first_user","first","last","first@test.com")
        projectUser.save()

        projectUser2 = ProjectUser()
        projectUser2.build_user("second_user","first","last","second@test.com")
        projectUser2.save()

        # Build a ticket
        t = Ticket()
        t.creator = projectUser
        t.name = "name"
        s = Status()
        s.name = "FakeState"
        s.save()
        t.status = s
        t.description = "description"
        t.open_date = datetime.datetime(2009, 12, 24)
        t.close_date = datetime.datetime(2010, 01, 29)
        t.priority = 3
        t.save()

        # build first comment
        c1 = t.comments.create(user = projectUser, message = "First")

        # build second comment
        c2 = t.comments.create(user = projectUser2, message = "Second")

        t.save()

        t2 = Ticket.objects.get(name="name")
        comments = t2.comments.all()
        self.failUnlessEqual("First",comments[0].message)

    def test_view_index(self):
        # Go to the tickets index page, should be a listing of all the tickets
        self.assertContains(self.get_view('index'), "First Ticket")
        self.assertContains(self.get_view('index'), "Second Ticket")
        # As a guest ISNBAT see a link to create a new ticket 
        self.assertNotContains(self.get_view('index'), "new ticket")
        # As a registered user ISBAT see a link to create a new ticket 
        self.log_in()
        self.assertContains(self.get_view('index'), "new ticket")

    def test_view_new(self):
        # As a guest ISNBAT access this view (should get redirected to home page)
        expected_url = "{0}?next={1}".format(reverse('users.views.login'), reverse('tickets.views.new'))
        self.assertRedirects(self.get_view('new'), expected_url)
        # As an authenticated user ISBAT to acces the view
        self.log_in()
        self.assertTemplateUsed(self.get_view('new'), 'tickets/new.html')
