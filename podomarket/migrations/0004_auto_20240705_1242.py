# Generated by Django 3.2.25 on 2024-07-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0003_auto_20240701_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='item_condition',
            field=models.CharField(choices=[('새제품', '새제품'), ('최상', '최상'), ('상', '상'), ('중', '중'), ('하', '하')], default=None, max_length=10),
        ),
    ]
