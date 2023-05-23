from django.db import models

from discussion.models import *


class CommunityModel(models.Model):
    id = models.UUIDField(verbose_name='id', primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, verbose_name='name')
    info = models.OneToOneField('CommunityInfoModel', on_delete=models.CASCADE, related_name='com_main', verbose_name='info', null=True)
    subscribers = models.ManyToManyField('my_user.User', related_name='sub_com')
    moderator = models.ManyToManyField('my_user.User', related_name='mod_com')

    def save(self, *args, **kwargs):
        super(CommunityModel, self).save(*args, **kwargs)


class CommunityInfoModel(models.Model):
    chapter = models.ForeignKey('my_user.User', on_delete=models.SET_NULL, null=True, verbose_name='chapter', related_name='chapter_com')
    avatar = models.ImageField(upload_to="community/avatar/%Y/%m/%d/", null=True, verbose_name='avatar')
    topic = models.CharField(max_length=200, verbose_name='topic', null=True)
    description = models.TextField(verbose_name='description', null=True)
    chat = models.OneToOneField('discussion.GroupChatsModel', on_delete=models.CASCADE, related_name='com_info', verbose_name='com_chat', null=True)


class CommunityPostModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    content = models.TextField(verbose_name='content')
    author = models.ForeignKey('my_user.User', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="community/post/%Y/%m/%d/", null=True, verbose_name='image')
    like = models.PositiveBigIntegerField(verbose_name='like', default=0)
    dislike = models.PositiveBigIntegerField(verbose_name='dislike', default=0)
    community = models.ForeignKey('CommunityModel', on_delete=models.CASCADE, related_name='community_post', null=True)



