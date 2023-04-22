from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', blank, name='Blank'),
    path('home/', home, name='Home'),
    path('actions/', actions, name='Actions'),
    path('action/<int:action_id>/', action, name='Action'),
    path('perform/action/<int:action_id>/', perform, name='Perform'),
    path('contact/', contact, name='Contact'),
    path('contact/messages/', contact_messages, name='Messages'),
    path('team/', team, name='Team'),
    path('login/', login, name='Login'),
    path('logout/', logout_user, name='Logout'),
]