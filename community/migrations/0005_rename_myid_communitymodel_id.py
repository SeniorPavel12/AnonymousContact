# Generated by Django 4.1.5 on 2023-01-19 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_rename_id_communitymodel_myid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communitymodel',
            old_name='myid',
            new_name='id',
        ),
    ]