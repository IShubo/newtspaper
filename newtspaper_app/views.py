from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests


# Create your views here.
def newtspaper_app(request):
    # make the request to newsapi
    # return the response

    API_KEY = "c467c532f88e46ddb2e6b2d6d4545cf5"
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {'articles': articles}
    return render(request, 'home.html', context)

def science(request):
    return render(request, 'science.html')


def business(request):
    return render(request, 'business.html')


def general(request):
    return render(request, 'general.html')


def sports(request):
    return render(request, 'sports.html')


def technology(request):
    return render(request, 'technology.html')


def yourPage(request):
    return render(request, 'yourPage.html')
