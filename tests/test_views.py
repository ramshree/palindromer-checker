from django.test import TestCase
from django.urls import reverse


class PalindromeViewsTest(TestCase):

    def test_valid_view(self):
        str = "palindrome_string"
        url = reverse("palindrome")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(str.encode('utf-8'), resp.content)