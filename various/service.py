from itertools import chain

from django.contrib.auth import get_user_model
from django.db.models import Q

import my_user
from community.models import *
from discussion.service import get_all_user
from my_user.models import User
from .models import *


def get_all_all_community():
    return CommunityModel.objects.all()


def search_user(content, my_user):
    con = content
    f = None if con.find(' ') == -1 else con.find(' ')
    name = content[:f].strip()
    if f is not None:
        surname = content[f:].strip()
    else:
        surname = ''
    print(name, surname)
    return User.objects.filter(
        Q(name=f"%{content}%") | Q(surname=f"%{content}%") | Q(username=f"%{content}%") | Q(name=f"{name}") | Q(
            surname=f"{surname}")).exclude(slug=my_user.slug)


def search_community(content):
    return CommunityModel.objects.filter(Q(name=f"%{content}%"))


def send_friend(my_user, user):
    user = user
    my_user = my_user
    if my_user not in user.sender_invite_notifications.all():
        try:
            notif = user.sender_invite_notifications.filter(sender_user=my_user).order_by('-time_create')[0] if bool(user.sender_invite_notifications.filter(sender_user=my_user).order_by('-time_create')) else False
            if notif:
                raise ValueError
            if notif.check_notification is True:
                if my_user.profile not in user.profile.subscribers.all():
                    user.profile.subscribers.add(my_user.profile)
                InviteNotificationsModel.objects.create(recipient_user=user, sender_user=my_user, type='SF', content=f'Вам предлагает подружиться {my_user.name} {my_user.surname}')
        except ValueError:
            if my_user.profile not in user.profile.subscribers.all():
                user.profile.subscribers.add(my_user.profile)
            InviteNotificationsModel.objects.create(recipient_user=user, sender_user=my_user, type='SF', content=f'Вам предлагает подружиться {my_user.name} {my_user.surname}')
        user.save()


def check_chat(my_user, user):
    if bool(ChatsModel.objects.filter(Q(first_user=user, second_user=my_user) | Q(first_user=my_user, second_user=user))) is False:
        return False
    else:
        return True


def check_subscriber(my_favourite_user, user):
    flag = True
    try:
        user.profile.subscribers.all().get(user=my_favourite_user)
    except my_user.models.user.ProfileInfoModel.DoesNotExist:
        flag = False
    return flag


def get_notifications(user):
    main = user.recipient_invite_notifications.all().order_by('-time_create')
    return main


def accept_friend(request):
    my_user = request.user
    user = get_user_model().objects.get(email=request.POST['accept_friend']).profile
    my_user.profile.subscribers.remove(user)
    my_user.profile.friends.add(user)
    notification = InviteNotificationsModel.objects.get(id=request.POST['id'])
    notification.check_notification = True
    notification.answer = True
    notification.save()


def reject_friend(request):
    notification = InviteNotificationsModel(id=request.POST['id'])
    notification.check_notification = True
    notification.answer = False
    notification.save()


def accept_community(request):
    my_user = request.user
    user = request.POST['accept_community']
    my_user.profile.sub_com.add(user)
    notification = InviteNotificationsModel(id=request.POST['id'])
    notification.check_notification = True
    notification.answer = True
    notification.save()


def reject_community(request):
    notification = InviteNotificationsModel(id=request.POST['id'])
    notification.check_notification = True
    notification.answer = False
    notification.save()


def accept_group(request):
    my_user = request.user
    user = request.POST['accept_group']
    my_user.profile.group_user.add(user)
    notification = InviteNotificationsModel(id=request.POST['id'])
    notification.check_notification = True
    notification.answer = True
    notification.save()


def reject_group(request):
    notification = InviteNotificationsModel(id=request.POST['id'])
    notification.check_notification = True
    notification.answer = False
    notification.save()
