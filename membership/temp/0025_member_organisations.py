# Generated by Django 4.0.1 on 2022-01-17 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_remove_churchorganisation_president'),
        ('membership', '0024_delete_nonfinancialdonation'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='organisations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.churchorganisation'),
        ),
    ]