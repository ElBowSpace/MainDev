from django.test import SimpleTestCase

class ViewTests(SimpleTestCase):

    def test_view_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

# Create your tests here.
