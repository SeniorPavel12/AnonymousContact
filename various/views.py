from django.contrib.auth import logout, login
from django.contrib.auth.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from community.service import *
from discussion.service import *
from my_user.form import *
from my_user.models import *
from my_user.service import *
from various.check_post import *
from various.service import *


class IndexView(View):
    def get(self, request):
        return redirect(reverse_lazy('user:profile'))


class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'registration/Login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = get_user_model().objects.get(email=form.cleaned_data.get("email"))
            password = form.cleaned_data.get("password")
            check_pass = user.check_password(password)
            if check_pass is True:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(reverse_lazy('user:profile'))
        return render(request, 'registration/Login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('various:login'))


class RegisterView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'registration/Register.html', {'form': UserRegisterForm})
        else:
            return redirect(reverse_lazy('user:profile'))

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('user:profile'))
        return render(request, 'registration/Register.html', {'form': form})


class SearchView(View):
    def get(self, request):
        user = get_user_model().objects.get(slug=request.user.slug)
        all_user = get_my_friends(user)
        all_community = get_all_all_community()
        answer, type_answer = None, None
        context = {
            'type_answer': type_answer,
            'answer': answer,
            'all_user': all_user,
            'all_community': all_community,
        }
        return render(request, 'various/Search.html', context=context)

    def post(self, request):
        user = get_user_model().objects.get(slug=request.user.slug)
        all_user = get_my_friends(user)
        all_community = get_all_all_community()
        answer, type_answer = check_post_SearchView(request)
        print(answer, type_answer)
        context = {
            'type_answer': type_answer,
            'answer': answer,
            'all_user': all_user,
            'all_community': all_community,
        }
        return render(request, 'various/Search.html', context=context)


class LookProfileView(View):
    def get(self, request, sluguser):
        my_user = get_user_model().objects.get(slug=request.user.slug)
        user = get_user_model().objects.get(slug=sluguser)
        chat_flag = check_chat(my_user, user)
        subscriber_flag = check_subscriber(my_user, user)
        context = {
            'subscriber_flag': subscriber_flag,
            'chat_flag': chat_flag,
            'user': user,
            'my_user': my_user,
        }
        return render(request, 'various/LookProfile.html', context=context)

    def post(self, request, sluguser):
        my_user = get_user_model().objects.get(slug=request.user.slug)
        user = get_user_model().objects.get(slug=sluguser)
        check_post_LookProfileView(request, my_user, user)
        chat_flag = check_chat(my_user, user)
        subscriber_flag = check_subscriber(my_user, user)
        context = {
            'subscriber_flag': subscriber_flag,
            'chat_flag': chat_flag,
            'user': user,
            'my_user': my_user,
        }
        return render(request, 'various/LookProfile.html', context=context)


class NotificationsView(View):
    def get(self, request):
        my_user = get_user_model().objects.get(slug=request.user.slug)
        notifications = get_notifications(my_user)
        context = {
            'notifications': notifications,
        }
        return render(request, 'various/Notifications.html', context=context)

    def post(self, request):
        my_user = get_user_model().objects.get(slug=request.user.slug)
        notifications = get_notifications(my_user)
        check_post_NotificationsView(request)
        context = {
            'notifications': notifications,
        }
        return render(request, 'various/Notifications.html', context=context)


class TestView(View):
    def get(self, request):
        res = {'name': 'Pasha', 'surname': 'Komandyshko'}
        return JsonResponse(res)
