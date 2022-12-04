from django.urls import path
from . import views

urlpatterns = [
    path('', views.newtspaper_app, name='newtspaper_app'),
    path('home', views.newtspaper_app, name='newtspaper_app'),
    path('science', views.science, name='science'),
    path('business', views.business, name='business'),
    path('general', views.general, name='general'),
    path('sports', views.sports, name='sports'),
    path('technology', views.technology, name='technology'),
    path('your-page', views.yourPage, name='your-page'),
]
