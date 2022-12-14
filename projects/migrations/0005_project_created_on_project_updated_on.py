# Generated by Django 4.0.1 on 2022-04-14 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_projectmonetarycontribution_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
