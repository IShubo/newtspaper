from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Articles, Profile
from .forms import ProfileForm


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
    API_KEY = "c467c532f88e46ddb2e6b2d6d4545cf5"
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {'articles': articles}
    return render(request, 'science.html', context)


def business(request):
    API_KEY = "c467c532f88e46ddb2e6b2d6d4545cf5"
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {'articles': articles}
    return render(request, 'business.html', context)


def general(request):
    API_KEY = "c467c532f88e46ddb2e6b2d6d4545cf5"
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {'articles': articles}
    return render(request, 'general.html', context)


def sports(request):
    API_KEY = "c467c532f88e46ddb2e6b2d6d4545cf5"
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {'articles': articles}
    return render(request, 'sports.html', context)


def technology(request):
    API_KEY = "c467c532f88e46ddb2e6b2d6d4545cf5"
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {'articles': articles}
    return render(request, 'technology.html', context)


@login_required()
def yourPage(request):
    profile = Profile.objects.all()
    context = {'profile': profile}
    return render(request, 'yourPage.html', context)


@login_required()
def edit_your_page(request, id):
    profile = Profile.objects.get(id=id)
    form = ProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'yourPage.html')

    context = {'form': form}
    return render(request, 'editYourPage.html', context)


@login_required()
def delete_your_page(request, id):
    profile = Profile.objects.filter(id=id)
    if request.method == 'POST':
        profile.update(data=None)
        return redirect('your-page')

    context = {'profile': profile}

    return render(request, 'yourPage.html', context)


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

# def search(request):
#     search_term = request.GET.get('search-term') or ''
#     tasks = Todo.objects.filter(task_name=search_term)
#     return render(request, 'todoList_app/index.html', {'tasks': tasks})

def searchResults(request):
    # if the request method is a post
    if request.method == 'POST':
        # get the search term and location
        search_term = request.POST.get('search_term')
        #location = request.POST.get('location')

        # You must enter your own API_KEY below
        API_KEY = "c467c532f88e46ddb2e6b2d6d4545cf5"

        # this is the url to access the endpoint yelp along with 2 parameters search term and location
        # more details can be found here https://www.yelp.com/developers/documentation/v3/business_search
        url = f'https://newsapi.org/v2/everything?q=+{search_term}+&apiKey={API_KEY}'
        print(url)
        # headers = {
        #     "Authorization": f"Bearer {API_KEY}"
        # }

    #     response = requests.get(url, headers=headers)
    #     data = response.json()
    #     total_results = data['total']
    #     businesses = data['businesses']
    #     return render(request, 'yelp/index-v2.html', {'businesses': businesses, 'total_results': total_results})
    # else:
    #     return render(request, 'yelp/index-v2.html')

        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        #total_results = data['total']  'total_results': total_results
        context = {'articles': articles}
        return render(request, 'searchResults.html', context)
    else:
        return render(request, 'home.html')


# @login_required
# def favorite_add(request, id):
#     article = get_object_or_404(Articles, id=id)
#     if article.favorites.filter(id=request.user.id).exists():
#         article.favorites.remove(request.user)
#     else:
#         article.favorites.add(request.user)
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])


# @login_required
# def favorite_list(request):
#     new = Articles.newmanager.filter(favorites=request.user)
#     context = {'new': new}
#     return render(request, 'favorites.html', context)