# Generated by Django 2.0.2 on 2018-11-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects_githublink'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
