# Generated by Django 4.1.1 on 2022-10-04 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_tasks_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='author',
            new_name='owner',
        ),
    ]
