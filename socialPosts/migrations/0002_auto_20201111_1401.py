# Generated by Django 3.1 on 2020-11-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialPosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialpost',
            name='title',
            field=models.CharField(default='---', max_length=256),
        ),
        migrations.AddField(
            model_name='socialpost',
            name='title_html',
            field=models.CharField(default='---', editable=False, max_length=256),
        ),
    ]
