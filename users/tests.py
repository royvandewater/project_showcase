from django.test import TestCaso

class UserTests(TestCase):

    def test_view_new(self):
        """
        Tests the user registration view
        """
        self.assertContains(self.client.get("/users/new/"), "Register", status_code=200)
