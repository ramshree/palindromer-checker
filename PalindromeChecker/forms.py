from django import forms


class PalindromeForm(forms.Form):
    palindrome_string = forms.CharField(required=True)