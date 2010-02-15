from django.test import TestCase

class UserTests(TestCase):
    fixtures = ['testdata']

    def test_view_new(self):
      """
        Tests the user registration view
      """
      self.assertContains(self.client.get("/users/new/"), "<h1>Register</h1>", status_code=200)
      self.assertContains(self.client.get("/users/new/"), "Confirm Password", status_code=200)
      # Try to submit with too-short passwords
      post_data = { 
          'email':'test@partybeat.net',
          'username':'test',
          'first_name':'first',
          'last_name':'last',
          'password':'pass',
          'confirm_password':'pass',
          }
      self.assertFormError(self.client.post("/users/new/", post_data), 'form', 'password', "Password must be at least 6 characters")
      # Try to submit with non-matching passwords
      post_data['password'] = "test_password"
      post_data['confirm_password'] = "test_password1"
      self.assertFormError(self.client.post("/users/new/", post_data), 'form', 'confirm_password', "Passwords do not match")
      self.assertFormError(self.client.post("/users/new/", post_data), 'form', 'email', "An account with that email address already exists")
      self.assertFormError(self.client.post("/users/new/", post_data), 'form', 'username', "That username is already taken")
      # register a legitimate user
      post_data['username'] = 'test1'
      post_data['email'] = 'something@random.net'
      post_data['confirm_password'] = post_data["password"]
      self.assertContains(self.client.post("/users/new/", post_data), "Thank you for registering", status_code=200)

    def test_view_login(self):
      """
      Tests the login view
      """
      self.assertContains(self.client.get("/users/login/"), "<h1>Login</h1>", status_code=200)
      self.assertContains(self.client.get("/users/login/"), "Username:", status_code=200)
      post_data = { 
              'username':'test',
              'password':'wrong_password',
              }
      self.assertContains(self.client.post("/users/login/", post_data), "Username/password combination not found", status_code=200)
      post_data = { 
              'username':'disabled',
              'password':'password',
              }
      self.assertContains(self.client.post("/users/login/", post_data), "Account has been disabled", status_code=200)
      post_data = { 
              'username':'test',
              'password':'password',
              }
      self.assertContains(self.client.post("/users/login/", post_data), "You are now logged in", status_code=200)
