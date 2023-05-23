from discussion.service import create_chat
from various.service import *


def check_post_SearchView(request):
    my_user = request.user
    if 'search_user' in request.POST:
        content = request.POST['content']
        return search_user(content, my_user), 'user'
    elif 'search_community' in request.POST:
        content = request.POST['content']
        return search_community(content), 'community'
    else:
        return None


def check_post_LookProfileView(request, my_user, user):
    if 'send_friend' in request.POST:
        send_friend(my_user, user)
    elif 'create_chat' in request.POST:
        create_chat(request, user)


def check_post_NotificationsView(request):
    if 'accept_friend' in request.POST:
        accept_friend(request)
    elif 'reject_friend' in request.POST:
        reject_friend(request)
    elif 'accept_community' in request.POST:
        accept_community(request)
    elif 'reject_friend' in request.POST:
        reject_friend(request)
    elif 'accept_group' in request.POST:
        accept_group(request)
    elif 'reject_friend' in request.POST:
        reject_friend(request)


