# Generated by Django 4.0.1 on 2022-01-17 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_externalmaterialdonation_externalmonetarydonation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='externalmaterialdonation',
            old_name='date_created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='externalmaterialdonation',
            old_name='date_updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='externalmonetarydonation',
            old_name='date_created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='externalmonetarydonation',
            old_name='date_updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='membermaterialdonation',
            old_name='date_created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='membermaterialdonation',
            old_name='date_updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='membermonetarydonation',
            old_name='date_created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='membermonetarydonation',
            old_name='date_updated',
            new_name='updated_on',
        ),
    ]
