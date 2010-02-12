from django.test import TestCase

class UserTests(TestCase):
    def check_response_code(self, url, code):
        """
        Check the url to ensure it returns the proper response code
        """
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, code)

    def test_view_new(self):
        """
        Tests the user registration view
        """
        self.check_response_code("/users/new/", 200)
