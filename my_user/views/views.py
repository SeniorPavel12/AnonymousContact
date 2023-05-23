from django.contrib.auth import logout, login
from django.contrib.auth.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from my_user.form import *
from my_user.models.user import *
from my_user.service import *
from my_user.utils import *
from my_user.check_post import *


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        my_user = get_user_model().objects.get(email=request.user.email)
        posts = my_user.profile.friends.all()
        user_id = my_user.slug
        friends = get_my_friends(my_user)
        context = {
            'posts': posts,
            'name': my_user.name,
            'surname': my_user.surname,
            'user_id': user_id,
            'age': my_user.profile.age,
            'status': my_user.profile.status,
            'friends': friends,
        }
        print(dir(request))
        return render(request, 'my_user/Profile.html', context=context)

    def post(self, request):
        my_user = get_user_model().objects.get(email=request.user.email)
        user_id = my_user.slug
        check_post_Profile(request, my_user)
        post = my_user.profile.post.all()
        friends = get_my_friends(my_user)
        context = {
            'posts': post,
            'name': my_user.name,
            'surname': my_user.surname,
            'user_id': user_id,
            'age': my_user.profile.age,
            'status': my_user.profile.status,
            'friends': friends,
        }
        return render(request, 'my_user/Profile.html', context=context)


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = get_user(request)
        user_id = user.id if user.name is None else user.username
        context = {
            'name': user.name,
            'surname': user.surname,
            'user_id': user_id,
            'username': user.username,
            'age': user.profile.age,
            'status': user.profile.status,
        }
        return render(request, 'my_user/EditProfile.html', context=context)

    def post(self, request):
        user = get_user(request)
        user_id = user.id if user.name is None else user.username
        check_post_EditProfile(request, user)
        context = {
            'name': user.name,
            'surname': user.surname,
            'user_id': user_id,
            'username': user.username,
            'age': user.profile.age,
            'status': user.profile.status,
        }
        return render(request, 'my_user/EditProfile.html', context=context)



