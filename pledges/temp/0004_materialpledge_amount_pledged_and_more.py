# Generated by Django 4.0.1 on 2022-01-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pledges', '0003_remove_materialpledge_amount_pledged_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialpledge',
            name='amount_pledged',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='membermaterialpledge',
            name='amount_pledged',
            field=models.FloatField(default=0.0),
        ),
    ]
