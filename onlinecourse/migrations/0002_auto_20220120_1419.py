# Generated by Django 3.1.3 on 2022-01-20 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='lesson',
            new_name='course',
        ),
    ]
