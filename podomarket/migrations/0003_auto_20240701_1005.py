# Generated by Django 3.2.25 on 2024-07-01 10:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import podomarket.validators


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0002_auto_20240624_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=40, null=True, validators=[podomarket.validators.validate_no_special_characters]),
        ),
        migrations.AlterField(
            model_name='user',
            name='kakao_id',
            field=models.CharField(max_length=20, null=True, validators=[podomarket.validators.validate_no_special_characters]),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 사용중인 닉네임입니다.'}, max_length=15, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('item_price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('item_condition', models.CharField(choices=[('새제품', '새제품'), ('최상', '최상'), ('상', '상'), ('중', '중'), ('히', '히')], max_length=10)),
                ('item_details', models.TextField(blank=True)),
                ('image1', models.ImageField(upload_to='item_pics')),
                ('image2', models.ImageField(blank=True, upload_to='item_pics')),
                ('image3', models.ImageField(blank=True, upload_to='item_pics')),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
