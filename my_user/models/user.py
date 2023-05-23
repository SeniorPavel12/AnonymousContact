import random
import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from my_user.manager import CustomUserManager


class ProfileInfoModel(models.Model):
    age = models.CharField(max_length=3, null=True)
    status = models.CharField(max_length=300, null=True)
    avatar_image = models.ImageField(upload_to="profile/avatar/%Y/%m/%d/", null=True)
    friends = models.ManyToManyField('self')
    subscribers = models.ManyToManyField('self', symmetrical=False)

    def save(self, *args, **kwargs):
        if self.age is None:
            self.age = random.choice(list(range(1, 100)))
        if self.status is None:
            self.status = random.choice(['Привет, как дела', 'Пицца, сериалы', 'Всё норм, а у тебя'])
        super(ProfileInfoModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'ProfileInfo'


class ProfilePostModel(models.Model):
    title = models.CharField(max_length=1000, verbose_name='title')
    content = models.TextField(verbose_name='content')
    image = models.ImageField(upload_to="profile/post/%Y/%m/%d/", null=True, verbose_name='image')
    author = models.ForeignKey(ProfileInfoModel, on_delete=models.CASCADE, null=True, related_name='post', verbose_name='author')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ProfilePost'


class User(AbstractUser):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4)
    username = models.CharField('username', max_length=700, null=True)
    email = models.EmailField("email address", unique=True)
    name = models.CharField('real name', max_length=200)
    surname = models.CharField('real surname', max_length=200)
    slug = models.SlugField('slug', unique=True, null=True)
    profile = models.OneToOneField(ProfileInfoModel, on_delete=models.CASCADE, null=True, related_name='user')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.username is None:
            self.username = self.id
        self.slug = slugify(self.username)
        if self.profile is None:
            self.profile = ProfileInfoModel.objects.create()
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('discussion:look_profile', kwargs={'user_slug': self.slug})

    class Meta:
        db_table = 'User'
