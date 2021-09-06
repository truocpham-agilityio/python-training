from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    tv_shows_list = {
        'tv_shows': {
            'Game of Thrones': '9.3',
            'Blacklist': '8',
            'Suits': '8.5',
            'The Witcher': '8.5'
        }
    }

    return render(request, 'first_app/index.html', context=tv_shows_list)


def home(request):
    return render(request, 'first_app/home.html')


def search(request):
    return render(request, 'first_app/search.html')


def about(request):
    return render(request, 'first_app/about.html')
