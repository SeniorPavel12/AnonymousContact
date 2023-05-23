from discussion.models import MessageModel
from .service import *


def check_post_ChatView(request, chat):
    if 'send_message' in request.POST:
        content = request.POST.get('send_message')
        send_message(request, content, chat)
    elif 'delete_all_message' in request.POST:
        id = request.POST.get('delete_all_message')
        delete_all_message(id)
    elif 'delete_me_message' in request.POST:
        id = request.POST.get('delete_me_message')
        delete_me_message(id, request)
    elif 'change_message' in request.POST:
        id = request.POST.get('change_message')
        content = request.POST.get('change_content_message')
        changing_message(id, content)


def check_post_ChatsView(request):
    if 'create_chat' in request.POST:
        slug = request.POST.get('create_chat')
        user = get_user(slug=slug)
        create_chat(request, user)
    elif 'create_group' in request.POST:
        title = request.POST['title_group']
        if title is not '':
            create_group(request, title)
    elif 'delete_chat' in request.POST:
        chat = ChatsModel.objects.get(id=int(request.POST['delete_chat']))
        delete_chat_for_user(request, chat)
    elif 'delete_group' in request.POST:
        group = get_group(request.POST['delete_group'])
        leave_group(request, group)


def check_post_GroupView(request, chat):
    if 'send_message' in request.POST:
        content = request.POST.get('send_message')
        send_group_message(request, content, chat)
    elif 'delete_all_message' in request.POST:
        id = request.POST.get('delete_all_message')
        delete_all_group_message(id)
    elif 'delete_me_message' in request.POST:
        id = request.POST.get('delete_me_message')
        delete_me_group_message(request, id)
    elif 'change_message' in request.POST:
        id = request.POST.get('change_message')
        content = request.POST.get('change_content_message')
        changing_group_message(id, content)
    elif 'add_user' in request.POST:
        user = get_user(slug=request.POST['add_user'])
        group_add_user(user, chat)
    elif 'delete_user' in request.POST:
        user = get_user(slug=request.POST['delete_user'])
        group_delete_user(user, chat)