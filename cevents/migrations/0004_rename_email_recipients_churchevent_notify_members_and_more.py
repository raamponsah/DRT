# Generated by Django 4.0.1 on 2022-06-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cevents', '0003_alter_churchevent_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='churchevent',
            old_name='email_recipients',
            new_name='notify_members',
        ),
        migrations.AddField(
            model_name='churchevent',
            name='venue',
            field=models.CharField(default='Church', max_length=255),
            preserve_default=False,
        ),
    ]
