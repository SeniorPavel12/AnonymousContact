import uuid

from django.db import models


class GroupMessageModel(models.Model):
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    user_create = models.ForeignKey('my_user.User', on_delete=models.CASCADE, related_name='create_group_message')
    unseeing = models.ManyToManyField('my_user.User')
    group = models.ForeignKey('GroupChatsModel', on_delete=models.CASCADE, related_name='group_message')


# class AnonymousMessageModel(models.Model):
#     content = models.TextField()
#     time_create = models.DateTimeField(auto_now_add=True)
#     user_create = models.SlugField(unique=False)
#     chat = models.ForeignKey('AnonymousChatsModel', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user_create


class MessageModel(models.Model):
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    user_create = models.ForeignKey('my_user.User', on_delete=models.CASCADE, related_name='create_chat_message')
    unseeing = models.ForeignKey('my_user.User', on_delete=models.CASCADE, null=True, related_name='unseeing_message')
    chat = models.ForeignKey('ChatsModel', on_delete=models.CASCADE, related_name='chat_message')

    def __str__(self):
        return self.user_create

    def save(self, *args, **kwargs):
        super(MessageModel, self).save(*args, **kwargs)


class ChatsModel(models.Model):
    first_user = models.ForeignKey('my_user.User', on_delete=models.CASCADE, related_name='first_author')
    second_user = models.ForeignKey('my_user.User', on_delete=models.CASCADE, related_name='second_author')
    unseeing = models.ManyToManyField('my_user.User', related_name='unseeing_chat')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_user.name[:10] + '&' + self.second_user.name[:10]


# class AnonymousChatsModel(models.Model):
#     first_user = models.SlugField()
#     second_user = models.SlugField()
#     first_nickname = models.SlugField()
#     second_nickname = models.SlugField()
#     time_create = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.first_user


class GroupChatsModel(models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    chapter = models.ForeignKey('my_user.User', on_delete=models.CASCADE, null=True, related_name='chapter_group')
    user = models.ManyToManyField('my_user.User', related_name='group_user')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


