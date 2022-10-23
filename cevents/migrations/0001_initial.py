# Generated by Django 4.0.1 on 2022-04-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('type', models.CharField(choices=[('one-time', 'One-Time'), ('recurring', 'Recurring')], default='one-time', max_length=20)),
                ('email_recipients', models.BooleanField(default=False)),
            ],
        ),
    ]
