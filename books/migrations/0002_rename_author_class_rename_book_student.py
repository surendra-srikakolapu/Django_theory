# Generated by Django 4.0.3 on 2022-04-20 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Class',
        ),
        migrations.RenameModel(
            old_name='Book',
            new_name='Student',
        ),
    ]