from django.shortcuts import render

from .models import HomeSlider

from skill.models import Skill, Showcase


def home(request):
    sliders = HomeSlider.objects.all().order_by('order')
    skills = Skill.objects.all().order_by('order')
    top_showcase = Showcase.objects.get(order=1)

    context = {
        'home': True,
        'sliders': sliders,
        'skills': skills,
        'top_showcase': top_showcase,
    }
    return render(request, 'personal/home.html', context)
