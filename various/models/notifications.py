from django.db import models


class NotificationsModelABC(models.Model):
    class TypeNotifications(models.TextChoices):
        SEND_FRIEND = 'SF', 'SendFriend'
        SEND_COMMUNITY = 'SC', 'SendCommunity'
        SEND_GROUP = 'SG', 'SendGroup'
        ADMIN_NEWS = 'AN', 'AdminNews'

    time_create = models.DateTimeField(null=True, auto_now_add=True, verbose_name='time create')
    content = models.CharField(max_length=1000, verbose_name='content')
    type = models.CharField(max_length=200, choices=TypeNotifications.choices, verbose_name='type')
    check_notification = models.BooleanField(default=False, verbose_name='check')

    class Meta:
        abstract = True


class InviteNotificationsModel(NotificationsModelABC):
    recipient_user = models.ForeignKey('my_user.User', on_delete=models.CASCADE, related_name='recipient_invite_notifications')
    sender_user = models.ForeignKey('my_user.User', on_delete=models.CASCADE, related_name='sender_invite_notifications', null=True)
    sender_group = models.ForeignKey('discussion.GroupChatsModel', on_delete=models.CASCADE, related_name='sender_invite_notifications', null=True)
    sender_community = models.ForeignKey('community.CommunityModel', on_delete=models.CASCADE, related_name='sender_invite_notifications', null=True)
    answer = models.BooleanField(default=False, verbose_name='answer')






