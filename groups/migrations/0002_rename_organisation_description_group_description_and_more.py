# Generated by Django 4.0.1 on 2022-04-11 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='organisation_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='organisation_name',
            new_name='name',
        ),
    ]