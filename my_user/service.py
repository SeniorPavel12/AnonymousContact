def get_my_friends(my_user):
    return my_user.profile.friends.all()
