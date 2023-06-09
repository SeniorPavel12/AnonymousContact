# Generated by Django 4.1.5 on 2023-01-19 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupChatsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=100)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapter_group', to=settings.AUTH_USER_MODEL)),
                ('user', models.ManyToManyField(related_name='group_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_message', to='discussion.groupchatsmodel')),
                ('unseeing', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('user_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_group_message', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='AnonymousChatsModel',
        ),
        migrations.DeleteModel(
            name='AnonymousMessageModel',
        ),
        migrations.AddField(
            model_name='chatsmodel',
            name='first_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='first_author', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatsmodel',
            name='second_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='second_author', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatsmodel',
            name='unseeing',
            field=models.ManyToManyField(related_name='unseeing_chat', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='unseeing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unseeing_message', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='user_create',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='create_chat_message', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_message', to='discussion.chatsmodel'),
        ),
    ]
