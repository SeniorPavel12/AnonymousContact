from django.urls import path

from .views import *

app_name = 'discussion'
urlpatterns = [
    # path('post/', PostView.as_view(), name='post'),
    path('chat/', ChatsView.as_view(), name='chats'),
    path('chat/<slug:sluguser>/', ChatView.as_view(), name='chat'),
    path('group/<slug:group_id>', GroupChatView.as_view(), name='group')
]









