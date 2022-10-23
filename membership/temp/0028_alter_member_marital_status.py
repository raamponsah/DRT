# Generated by Django 4.0.1 on 2022-01-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0027_member_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('co-habitating', 'Co-habitating'), ('engaged', 'Engaged'), ('separated', 'Separated'), ('divorced', 'Divorced'), ('religious', 'religious')], default=('single', 'Single'), max_length=20),
        ),
    ]