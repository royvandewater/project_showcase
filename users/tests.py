from django.test import TestCase

class UserTests(TestCase):
    fixtures = ['testdata']

    def test_view_new(self):
        """
        Tests the user registration view
        """
        self.assertContains(self.client.get("/users/new/"), "<h1>Register</h1>", status_code=200)
        self.assertContains(self.client.get("/users/new/"), "Confirm Password", status_code=200)
