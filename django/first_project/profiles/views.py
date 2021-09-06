from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Profiles page!')

def profile_page(request, id):
    return HttpResponse('Profile ID: %s' % id)
