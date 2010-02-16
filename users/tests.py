from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core import mail

class UserTests(TestCase):
    fixtures = ['testdata']

    def get_view(self, url):
      return self.client.get(reverse("users.views.{0}".format(url)))

    def post_view(self, url, post_data):
      return self.client.post(reverse("users.views.{0}".format(url)), post_data)

    def test_view_new(self):
      """
        Tests the user registration view
      """
      self.assertContains(self.get_view("new"), "<h1>Register</h1>", status_code=200)
      self.assertContains(self.get_view("new"), "Confirm Password", status_code=200)
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
      self.assertContains(self.post_view("new", post_data), "Thank you for registering", status_code=200)

    def test_view_login(self):
      """
      Tests the login view
      """
      self.assertContains(self.get_view("login"), "<h1>Login</h1>", status_code=200)
      self.assertContains(self.get_view("login"), "Username:", status_code=200)
      post_data = { 
              'username':'test',
              'password':'wrong_password',
              }
      self.assertContains(self.post_view("login", post_data), "Username/password combination not found", status_code=200)
      post_data = { 
              'username':'disabled',
              'password':'password',
              }
      self.assertContains(self.post_view("login", post_data), "Account has been disabled", status_code=200)
      post_data = { 
              'username':'test',
              'password':'password',
              }
      self.assertContains(self.post_view("login", post_data), "You are now logged in", status_code=200)

    def test_view_forgot(self):
      """
      Tests the password reset view
      """
      self.assertContains(self.get_view('reset'), "Enter your email address and you will receive", status_code=200)
      self.assertContains(self.get_view('reset'), "Email address:", status_code=200)
      # Test email required
      post_data = {
              'email':'',
              }
      self.assertFormError(self.post_view("new", post_data), 'form', 'password', "This field is required.")
      post_data = {
              'email':'test@fail.com',
              }
      self.assertContains(self.post_view('reset', post_data), "There does not exist an account with that email address", status_code=200)
      post_data = {
              'email':'test@partybeat.net',
              }
      self.assertContains(self.post_view('reset', post_data), "An email with the reset link has been sent", status_code=200)
      # Check to see if the email was actually sent
      self.assertEqual(len(mail.outbox), 1)

