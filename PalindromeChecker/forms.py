from django import forms


class PalindromeForm(forms.Form):
    word = forms.CharField(required=True)
