from my_user.models import ProfilePostModel


def check_post_EditProfile(request, user):
    if 'name' in request.POST:
        user.name = request.POST['name']
        user.save()
    if 'surname' in request.POST:
        user.surname = request.POST['surname']
        user.save()
    if 'username' in request.POST:
        user.username = request.POST['username']
        user.save()
    if 'age' in request.POST:
        user.age = request.POST['age']
        user.save()
    if 'status' in request.POST:
        user.status = request.POST['status']
        user.save()


def check_post_Profile(request, user):
    if 'post' in request.POST:
        title = request.POST['title']
        content = request.POST['content']
        author = user.profile
        ProfilePostModel.objects.create(title=title, content=content, author=author)
