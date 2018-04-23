from django.http import HttpResponse
from PalindromeChecker.forms import PalindromeForm
from django.shortcuts import render
from PalindromeChecker import palindrome as p


def palindrome(request):
    form = PalindromeForm

    if request.method == 'POST':
        form = PalindromeForm(request.POST)

        if form.is_valid():
            s_query = form.cleaned_data['word']
            if p.Palindrome.palindrome_check(s_query):
                s_results = s_query + " is a palindrome!!"
            else:
                s_results = s_query + " is not a palindrome!!"

            return render(request, 'palindrome.html', {'form': form, 's_results': s_results})
        else:
            return HttpResponse("no thank you")
    else:
        return render(request, 'palindrome.html', {'form': form, })