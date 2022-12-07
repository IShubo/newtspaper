from django.urls import path
from . import views

urlpatterns = [
    path('', views.newtspaper_app, name='newtspaper_app'),
    path('home', views.newtspaper_app, name='home'),
    path('science', views.science, name='science'),
    path('business', views.business, name='business'),
    path('general', views.general, name='general'),
    path('sports', views.sports, name='sports'),
    path('technology', views.technology, name='technology'),
    path('your-page', views.yourPage, name='your-page'),


    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
