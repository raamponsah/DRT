# Generated by Django 4.0.1 on 2022-04-15 17:04

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_projectdocument_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdocument',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdocument',
            name='document_upload',
            field=models.FileField(blank=True, null=True, upload_to=projects.models.document_path_directory),
        ),
    ]
