from django.test import TestCase

class SimpleTest(TestCase):
    fixtures = ['testdata']

    def url(self, url):
        return self.client.get("/about%s" % (url))


    def test_about_page(self):
        """
        Test to see if about page still shows
        """
        self.assertContains(self.url('/'), "<h1>About Partybeat</h1>",  status_code=200)
