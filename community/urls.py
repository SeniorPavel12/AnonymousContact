from django.urls import path

from .views import *

app_name = 'community'
urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
    path('', CommunityView.as_view(), name='community'),
    path('<slug:com_id>/', CommunityServerView.as_view(), name='community_server'),
]
