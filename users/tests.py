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
                'display_name':'test',
                'password':'pass',
                'confirm_password':'pass',
                }
        self.assertContains(self.client.post("/users/new/", post_data), "Password must be at least 6 characters", status_code=200)
        # Try to submit with non-matching passwords
        post_data['password'] = "test_password"
        post_data['confirm_password'] = "test_password1"
        self.assertContains(self.client.post("/users/new/", post_data), "Passwords do not match", status_code=200)
        # register a legitimate user
        post_data['confirm_password'] = post_data["password"]
        self.assertContains(self.client.post("/users/new/", post_data), "Thank you for registering", status_code=200)
