# Generated by Django 2.0.2 on 2018-11-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='githubLink',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
