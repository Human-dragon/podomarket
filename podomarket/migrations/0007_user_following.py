# Generated by Django 3.2.25 on 2024-07-24 10:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
