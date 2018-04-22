from django.test import TestCase


class PalindromeTest(TestCase):

    def test_plalindrome_success(self):
        self.assertTrue("SAS")

    def test_palindrome_failure(self):
        self.assertTrue("SAs")