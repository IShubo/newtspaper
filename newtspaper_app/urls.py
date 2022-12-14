from django.template.defaulttags import url
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
    path('edit-your-page/<int:id>', views.edit_your_page, name='edit-your-page'),
    path('delete-your-page/<int:id>', views.delete_your_page, name='delete-your-page'),
    path('searchResults/', views.searchResults, name='searchResults'),
    # path('fav/<int:id>', views.favorite_add, name='favoriteAdd'),
    # path('fav/favList', views.favorite_list, name='favoriteList'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
