from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


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


# Register a user
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# Log a user in
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
