# Generated by Django 4.0.1 on 2022-01-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0014_trackdailyactivities_total_levies_collected_today'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='father_living_status',
            field=models.BooleanField(choices=[('deceased', 'Deceased'), ('alive', 'Alive')], default=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='mother_living_status',
            field=models.BooleanField(choices=[('deceased', 'Deceased'), ('alive', 'Alive')], default=True),
        ),
    ]
