# Generated by Django 4.0.4 on 2022-07-28 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='images',
            new_name='image',
        ),
    ]