# Generated by Django 3.2.10 on 2021-12-21 18:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Task_Manager', '0003_auto_20211221_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
