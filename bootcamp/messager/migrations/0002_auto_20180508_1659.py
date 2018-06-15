# Generated by Django 2.0.3 on 2018-05-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='is_read',
        ),
        migrations.AddField(
            model_name='message',
            name='unread',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
