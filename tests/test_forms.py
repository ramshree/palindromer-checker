from django.test import TestCase
from PalindromeChecker.forms import PalindromeForm


class PalindromeFormsTest(TestCase):

    def test_valid_form(self):
        data = {'palindrome_string': "SAS"}
        form = PalindromeForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'palindrome_string': ""}
        form = PalindromeForm(data=data)
        self.assertFalse(form.is_valid())