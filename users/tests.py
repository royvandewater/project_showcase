from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core import mail

import re

from models import *

class UserTests(TestCase):
    fixtures = ['testdata']
    reset_url = None

    def get_view(self, url):
      return self.client.get(reverse("users.views." + url))

    def post_view(self, url, post_data):
      return self.client.post(reverse("users.views." + url), post_data)

    def test_model_projectUser(self):
        """
        Tests the projectUser model
        """
        projectUser = ProjectUser()
        user = User()
        user.username = "testuser"
        user.first_name = "first"
        user.last_name = "last"
        user.email = "test@test.com"
        user.save()
        projectUser.user = user
        projectUser.reset_string = "test reset string"
        projectUser.save()
        pu2 = ProjectUser.objects.get(reset_string="test reset string")
        self.assertEqual(pu2.user, projectUser.user)
        self.assertEqual(str(pu2), "testuser (first last)")

    def test_view_new(self):
      """
        Tests the user registration view
      """
      self.assertContains(self.get_view("new"), "<h1>Register</h1>")
      self.assertContains(self.get_view("new"), "Confirm Password")
      # Try to submit with too-short passwords
      post_data = { 
          'email':'test@partybeat.net',
          'username':'test',
          'first_name':'first',
          'last_name':'last',
          'password':'pass',
          'confirm_password':'pass',
          }
      self.assertFormError(self.post_view("new", post_data), 'form', 'password', "Password must be at least 6 characters")
      # Try to submit with no passwords
      post_data['password'] = post_data['confirm_password'] = ""
      self.assertFormError(self.post_view("new", post_data), 'form', 'password', "This field is required.")
      # Try to submit with non-matching passwords
      post_data['password'] = "test_password"
      post_data['confirm_password'] = "test_password1"
      self.assertFormError(self.post_view("new", post_data), 'form', 'confirm_password', "Passwords do not match")
      self.assertFormError(self.post_view("new", post_data), 'form', 'email', "An account with that email address already exists")
      self.assertFormError(self.post_view("new", post_data), 'form', 'username', "That username is already taken")
      # register a legitimate user
      post_data['username'] = 'test1'
      post_data['email'] = 'something@random.net'
      post_data['confirm_password'] = post_data["password"]
      self.assertContains(self.post_view("new", post_data), "Thank you for registering")

    def test_view_login(self):
      """
      Tests the login view
      """
      self.assertContains(self.get_view("login"), "<h1>Login</h1>")
      self.assertContains(self.get_view("login"), "Username:")
      post_data = { 
              'username':'test',
              'password':'wrong_password',
              }
      self.assertContains(self.post_view("login", post_data), "Username/password combination not found")
      post_data = { 
              'username':'disabled',
              'password':'password',
              }
      self.assertContains(self.post_view("login", post_data), "Account has been disabled")
      post_data = { 
              'username':'test',
              'password':'password',
              }
      self.assertContains(self.post_view("login", post_data), "You are now logged in")

    def test_view_destroy(self):
        """
        Tests the logout functionality
        """
        self.assertRedirects(self.get_view('destroy'), reverse('news.views.index'))

    def test_view_forgot(self):
      """
      Tests the password reset view
      """
      self.assertContains(self.get_view('forgot'), "Enter your email address and you will receive")
      self.assertContains(self.get_view('forgot'), "Email address:")
      # Test email required
      post_data = {
              'email':'',
              }
      self.assertFormError(self.post_view("forgot", post_data), 'form', 'email', "This field is required.")
      post_data = {
              'email':'test@fail.com',
              }
      self.assertContains(self.post_view('forgot', post_data), "There does not exist an account with that email address")
      post_data = {
              'email':'test@partybeat.net',
              }
      self.assertContains(self.post_view('forgot', post_data), "An email with the reset link has been sent")
      # Check to see if the email was actually sent
      self.assertEqual(len(mail.outbox), 1)
      reset_url = re.search("http:\/\/example\.com(?P<address>.*)", mail.outbox[0].body).group('address')
      # Try a random url that we know will fail
      url = reverse('users.views.reset', kwargs={'email':'test@partybeat.com', 'reset_string':'qzt'})
      self.assertContains(self.client.get(url), "The email address or reset key is incorrect.")
      # Get the reset string from mail
      self.assertContains(self.client.get(reset_url), "Please enter a new password")
      post_data = {
              'password':'new_pass',
              'confirm_password':'old_pass',
              }
      self.assertFormError(self.client.post(reset_url, post_data), 'form', 'confirm_password', "Passwords do not match")
      post_data = {
              'password':'new_pass',
              'confirm_password':'new_pass',
              }
      self.assertContains(self.client.post(reset_url, post_data), "Your password has been updated.")
      self.assertContains(self.client.get(reset_url), "Please use the url provided in")
      post_data = { 
              'username':'test',
              'password':'new_pass',
              }
      self.assertContains(self.post_view("login", post_data), "You are now logged in")
