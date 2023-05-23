from uuid import uuid4

from django.db.models import Q

from discussion.models import *
from my_user.models import *


def get_chats(request):
    chats = ChatsModel.objects.filter(Q(first_user=request.user) | Q(second_user=request.user))
    return chats


def get_all_user(request):
    return User.objects.exclude(email=request.user.email)


def get_user_id(user):
    if user.username is None:
        return user.id
    else:
        return user.username


def create_chat(request, user):
    if bool(ChatsModel.objects.filter(Q(first_user=request.user, second_user=user) | Q(first_user=user, second_user=request.user))) is False:
        ChatsModel.objects.create(first_user=request.user, second_user=user)
    else:
        chat = ChatsModel.objects.get(Q(first_user=request.user, second_user=user) | Q(first_user=user, second_user=request.user))
        chat.unseeing.remove(request.user)
        chat.save()


def get_user(email=None, slug=None):
    if slug is None:
        return User.objects.get(email=email)
    if email is None:
        return User.objects.get(slug=slug)


def get_chat(sluguser, request):
    first_user = get_user(slug=sluguser)
    second_user = get_user(slug=request.user.slug)
    return ChatsModel.objects.get(Q(first_user=first_user, second_user=second_user) | Q(first_user=second_user, second_user=first_user))


def send_message(request, content, chat):
    MessageModel.objects.create(content=content, user_create=request.user, chat=chat)


def changing_message(id, content):
    message = MessageModel.objects.get(pk=int(id))
    message.content = str(content)
    message.save()


def delete_all_message(id):
    message = MessageModel.objects.get(pk=int(id))
    message.delete()


def delete_me_message(request, id):
    message = MessageModel.objects.get(pk=int(id))
    if message.unseeing is None:
        message.unseeing = request.user.slug
        message.save()
    else:
        message.delete()


def get_message(request, chat, sluguser):
    return MessageModel.objects.filter(chat=chat)


def create_group(request, title):
    user = (request.user, )
    g = GroupChatsModel.objects.create(chapter=request.user, title=title)
    g.user.set(user)
    g.save()


def get_group(id):
    return GroupChatsModel.objects.get(id=id)


def get_group_message(group_id, request):
    group = GroupChatsModel.objects.get(id=group_id)
    return GroupMessageModel.objects.filter(group=group).exclude(unseeing=request.user)


def send_group_message(request, content, group):
    user_create = request.user
    GroupMessageModel.objects.create(content=content, user_create=user_create, group=group)


def get_all_group(request):
    user = request.user
    return GroupChatsModel.objects.filter(user=user)


def changing_group_message(id, content):
    message = MessageModel.objects.get(pk=int(id))
    message.content = str(content)
    message.save()


def delete_all_group_message(id):
    message = GroupMessageModel.objects.get(pk=int(id))
    message.delete()


def delete_me_group_message(request, id):
    message = GroupMessageModel.objects.get(pk=int(id))
    message.unseeing.add(request.user)
    message.save()


def group_add_user(user, chat):
    chat.user.add(user)
    chat.save()


def get_group_user(group):
    return group.user.all()


def delete_chat_for_user(request, chat):
    user = request.user
    chat.unseeing.add(user)
    chat.save()
    print(chat.unseeing.all())


def leave_group(request, group):
    user = request.user
    group.user.remove(user)
    group.save()




