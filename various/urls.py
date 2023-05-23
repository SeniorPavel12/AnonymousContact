
from django.urls import path

from .views import *

app_name = 'various'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('search/', SearchView.as_view(), name='search'),
    path('profile/<slug:sluguser>', LookProfileView.as_view(), name='look_profile'),
    path('notifications/', NotificationsView.as_view(), name='notifications'),
    path('test/', TestView.as_view(), name='test'),
    ]



