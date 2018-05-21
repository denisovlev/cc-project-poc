# Generated by Django 2.0.5 on 2018-05-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_email_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200, verbose_name='link')),
                ('size', models.IntegerField(verbose_name='size')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('mime', models.CharField(max_length=200, verbose_name='mime')),
                ('content', models.BinaryField(verbose_name='content')),
                ('posts', models.ManyToManyField(to='main.Post')),
            ],
        ),
    ]
