from django.contrib.auth import get_user_model


def get_user(request):
    return get_user_model().objects.get(email=request.user.email)
