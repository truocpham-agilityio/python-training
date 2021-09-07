from django.shortcuts import render
from django.http import HttpResponse
from first_app.forms import TestForm

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


def forms(request):
    initial_dict = {
        'text': 'Some initial data',
        'integer': 123,
    }
    form = TestForm(request.POST or None, initial=initial_dict)
    data = 'None'
    text = 'None'

    if form.is_valid():
        data = form.cleaned_data
        text = form.cleaned_data.get('text')

    return render(request, 'first_app/forms.html', {'form': form, 'data': data, 'text': text})
