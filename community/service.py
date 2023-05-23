from django.contrib.auth import get_user_model
from itertools import chain

from django.db.models import QuerySet

from community.models import *
from discussion.service import *
from various.models import InviteNotificationsModel


def get_post(user):
    sub, mod = user.sub_com.all(), user.mod_com.all()
    sup = list(chain(list(chain(i.community_post.all())) for i in sub)) + list(chain(list(chain(j.community_post.all())) for j in mod))
    main = []
    for i in sup:
        main.extend(i)
    return main


def get_sub_community(request):
    user = get_user(slug=request.user.slug)
    return list(chain(user.sub_com.all()))


def get_mod_community(request):
    user = get_user(slug=request.user.slug)
    return list(chain(user.chapter_com.all(), user.mod_com.all()))


def create_community(request):
    name = request.POST['name']
    if name is not None:
        topic = request.POST['topic']
        description = request.POST['description']
        chapter = request.user
        com = CommunityModel.objects.create(name=name, info=CommunityInfoModel.objects.create(topic=topic, description=description, chapter=chapter))
        com.moderator.set((request.user, ))
        if 'chat' in request.POST:
            com.info.chat = GroupChatsModel.objects.create(chapter=chapter, title=name)
            com.info.chat.user.set((request.user,))
        com.save()


def get_community(id):
    return CommunityModel.objects.get(id=id)


def get_community_post(id):
    com = get_community(id=id)
    return com.community_post.all()


def get_community_subscribers(request, id):
    com = get_community(id)
    user = request.user
    return com.subscribers.all().exclude(slug=user.slug)


def get_community_moderator(request, id):
    com = get_community(id)
    user = request.user
    return com.moderator.all().exclude(slug=user.slug)


def get_all_community(request):
    user = request.user
    return CommunityModel.objects.exclude(Q(moderator=user) | Q(subscribers=user))


def join_community(request):
    id = request.POST['join_com']
    user = request.user
    com = CommunityModel.objects.get(id=id)
    com.subscribers.add(user)
    com.save()


def add_moderator(user, com):
    com.moderator.add(user)
    com.subscribers.remove(user)
    com.save()


def delete_moderator(user, com):
    com.moderator.remove(user)
    com.subscribers.add(user)
    com.save()

def create_community_post(title, content, author, com):
    CommunityPostModel.objects.create(title=title, content=content, author=author, community=com)


def get_friend(request):
    return request.user.profile.friends.all()


def add_friend_to_community(request, com):
    my_user = request.user
    user = get_user_model().objects.all(id=request.POST['add_user'])
    if com not in user.sender_invite_notifications.all():
        try:
            notif = user.sender_invite_notifications.filter(sender_community=com).order_by('-time_create')[0] if bool(user.sender_invite_notifications.filter(sender_community=com).order_by('-time_create')) is True else False
            if notif is False:
                raise ValueError
            if notif.check_notification is True:
                InviteNotificationsModel.objects.create(recipient_user=user, sender_community=com, type='SC', content=f'Вас приглашают в сообщество {com.name}')
        except ValueError:
            InviteNotificationsModel.objects.create(recipient_user=user, sender_community=com, type='SC', content=f'Вас приглашают в сообщество {com.name}')
        user.save()




