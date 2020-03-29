from django.shortcuts import render

from .models import Profile


def contact(request):
    context = {
        'contact': True,
    }
    return render(request, 'account/contact.html', context)
