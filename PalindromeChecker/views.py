from django.http import HttpResponse
from PalindromeChecker.forms import PalindromeForm


from django.shortcuts import render


def palindrome(request):
    form_class = PalindromeForm

    if request.method == 'POST':
        form = PalindromeForm(request.POST)

        if form.is_valid():
            if palindrome_check(form.cleaned_data['palindrome_string']):
                return HttpResponse(form.cleaned_data['palindrome_string'] + " is a palindrome!!")
            else:
                return HttpResponse(form.cleaned_data['palindrome_string'] + " is not a palindrome!!")
        else:
            return HttpResponse("no thank you")
    else:
        return render(request, 'palindrome.html', {
            'form': form_class

    })


def palindrome_check(n):
    return str(n) == str(n)[::-1]