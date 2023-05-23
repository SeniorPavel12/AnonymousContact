from uuid import UUID

from django.shortcuts import render
from django.views import View

from community.check_post import *
from community.service import *


# Create your views here.


class PostView(View):
    def get(self, request):
        my_user = request.user
        all_post = get_post(my_user)
        context = {
            'post': all_post
        }
        print(all_post)
        return render(request, 'community/Post.html', context=context)

    def post(self, request):
        my_user = request.user
        all_post = get_post(my_user)
        context = {
            'post': all_post
        }
        return render(request, 'community/Post.html', context=context)


class CommunityView(View):
    def get(self, request):
        all_community = get_all_community(request)
        my_community = list(chain(get_mod_community(request), get_sub_community(request)))
        context = {
            'my_community': my_community,
            'all_community': all_community,
        }
        return render(request, 'community/Community.html', context=context)

    def post(self, request):
        check_post_CommunityView(request)
        all_community = get_all_community(request)
        my_community = list(chain(get_mod_community(request), get_sub_community(request)))
        context = {
            'my_community': my_community,
            'all_community': all_community,
        }
        return render(request, 'community/Community.html', context=context)


class CommunityServerView(View):
    def get(self, request, com_id):
        com = get_community(com_id)
        post = get_community_post(com_id)
        subscribers = get_community_subscribers(request, com_id)
        moderator = get_community_moderator(request, com_id)
        my_user = request.user
        is_moderator = False if bool(my_user.mod_com.filter(id=com_id)) is False else True
        is_subscriber = False if bool(my_user.sub_com.filter(id=com_id)) is False else True
        is_chapter = False if bool(my_user.chapter_com.all()) is False else True
        friend = get_friend(request)
        context = {
            'friend': friend,
            'com': com,
            'post': post,
            'subscribers': subscribers,
            'moderator': moderator,
            'my_user': my_user,
            'is_moderator': is_moderator,
            'is_subscriber': is_subscriber,
            'is_chapter': is_chapter,
        }
        return render(request, 'community/CommunityServer.html', context=context)

    def post(self, request, com_id):
        com = get_community(com_id)
        post = get_community_post(com_id)
        subscribers = get_community_subscribers(request, com_id)
        moderator = get_community_moderator(request, com_id)
        my_user = request.user
        is_moderator = my_user.mod_com.filter(id=com_id)
        is_subscriber = my_user.sub_com.filter(id=com_id)
        is_chapter = my_user.chapter_com.filter(com_main__id=com_id)
        check_post_CommunityServerView(request, com)
        friend = get_friend(request)
        print(friend)
        context = {
            'friend': friend,
            'com': com,
            'post': post,
            'subscribers': subscribers,
            'moderator': moderator,
            'my_user': my_user,
            'is_moderator': is_moderator,
            'is_subscriber': is_subscriber,
            'is_chapter': is_chapter,
        }
        return render(request, 'community/CommunityServer.html', context=context)