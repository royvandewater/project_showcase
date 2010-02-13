from django.test import TestCase

class UserTests(TestCase):

    def test_view_new(self):
        """
        Tests the user registration view
        """
        self.assertContains(self.client.get("/users/new/"), "<h2>Register</h2>", status_code=200)
