from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from my_user.models import *
from .forms import *
from .service import *
from .check_post import *


class ChatsView(LoginRequiredMixin, View):
    def get(self, request):
        chats = get_chats(request)
        all_user = get_all_user(request)
        group = get_all_group(request)
        context = {
            'my_user': request.user,
            'groups': group,
            'chats': chats,
            'all_user': all_user,
        }
        return render(request, 'discussion/Chats.html', context=context)

    def post(self, request):
        chats = get_chats(request)
        all_user = get_all_user(request)
        check_post_ChatsView(request)
        group = get_all_group(request)
        context = {
            'my_user': request.user,
            'groups': group,
            'chats': chats,
            'all_user': all_user,
        }
        return render(request, 'discussion/Chats.html', context=context)


class ChatView(LoginRequiredMixin, View):
    def get(self, request, sluguser):
        user = get_user(slug=sluguser)
        chat = get_chat(sluguser, request)
        check_post_ChatView(request, chat)
        messages = get_message(request, chat, sluguser)
        context = {
            'my_user': request.user,
            'user': user,
            'chat': chat,
            'messages': messages,
        }
        return render(request, 'discussion/Chat.html', context=context)

    def post(self, request, sluguser):
        user = get_user(slug=sluguser)
        chat = get_chat(sluguser, request)
        check_post_ChatView(request, chat)
        messages = get_message(request, chat, sluguser)
        context = {
            'my_user': request.user,
            'user': user,
            'chat': chat,
            'messages': messages,
        }
        return render(request, 'discussion/Chat.html', context=context)


class GroupChatView(View):
    def get(self, request, group_id):
        group = get_group(group_id)
        message = get_group_message(group_id, request)
        all_user = get_all_user(request)
        group_user = get_group_user(group)
        context = {
            'user_is_chapter': True if group.chapter == request.user else False,
            'group_user': group_user,
            'all_user': all_user,
            'group': group,
            'messages': message,
            'user': request.user
        }
        return render(request, 'discussion/Group.html', context=context)

    def post(self, request, group_id):
        group = get_group(group_id)
        message = get_group_message(group_id, request)
        check_post_GroupView(request, group)
        all_user = get_all_user(request)
        group_user = get_group_user(group)
        context = {
            'user_is_chapter': True if group.chapter == request.user else False,
            'group_user': group_user,
            'all_user': all_user,
            'group': group,
            'messages': message,
            'user': request.user
        }
        return render(request, 'discussion/Group.html', context=context)
