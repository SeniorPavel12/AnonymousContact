from community.service import *


def check_post_CommunityView(request):
    if 'join_com' in request.POST:
        join_community(request)

def check_post_CommunityServerView(request, com):
    if 'create_community' in request.POST:
        create_community(request)
    elif 'update_moderator' in request.POST:
        if 'add_moderator' in request.POST:
            user = request.POST['add_moderator']
            add_moderator(user, com)
        if 'delete_moderator' in request.POST:
            user = request.POST['delete_moderator']
            delete_moderator(user, com)
    elif 'create_post' in request.POST:
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        create_community_post(title, content, author, com)
    elif 'add_friend' in request.POST:
        add_friend_to_community(request, com)