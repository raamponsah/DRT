# Generated by Django 4.0.1 on 2022-01-26 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pledges', '0009_alter_materialpledge_redeemed_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membermaterialpledge',
            name='description',
        ),
        migrations.RemoveField(
            model_name='membermaterialpledge',
            name='item',
        ),
        migrations.RemoveField(
            model_name='membermaterialpledge',
            name='quantity',
        ),
    ]
