from django.contrib.auth.views import LogoutView
from django.urls import path

from .views.views import *

app_name = 'user'
urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),

 ]


