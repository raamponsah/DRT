# Generated by Django 4.0.1 on 2022-01-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipmonthlylevy',
            name='total',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
