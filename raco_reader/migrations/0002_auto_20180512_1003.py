# Generated by Django 2.0.5 on 2018-05-12 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raco_reader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]