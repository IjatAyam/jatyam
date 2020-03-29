from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Showcase


def showcase(request):
    showcases = Showcase.objects.all().order_by('order')
    paginator = Paginator(showcases, 4)
    page = request.GET.get('page')
    showcases = paginator.get_page(page)

    context = {
        'show': True,
        'showcases': showcases,
    }
    return render(request, 'skill/showcase.html', context)
