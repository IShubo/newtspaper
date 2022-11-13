from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def newtspaper_app(request):
    return render(request, 'home.html')


def science(request):
    return render(request, 'science.html')


def business(request):
    return render(request, 'business.html')


def currentEvents(request):
    return render(request, 'currentEvents.html')


def sports(request):
    return render(request, 'sports.html')


def technology(request):
    return render(request, 'technology.html')


def yourPage(request):
    return render(request, 'yourPage.html')
