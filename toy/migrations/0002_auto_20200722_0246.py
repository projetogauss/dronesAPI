# Generated by Django 3.0.8 on 2020-07-22 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toy',
            old_name='release_date',
            new_name='realease_date',
        ),
    ]