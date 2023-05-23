from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class DiscussionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'discussion'

class MyAdminConfig(AdminConfig):
    default_site = 'discussion.admin.MyAdminSite'
