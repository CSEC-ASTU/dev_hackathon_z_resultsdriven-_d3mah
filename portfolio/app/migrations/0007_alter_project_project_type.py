# Generated by Django 4.1.5 on 2023-06-10 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_project_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('Web Development', 'Web Development'), ('Modules', 'Modules'), ('Machine Learning', 'Machine Learning'), ('Publication', 'Publication')], max_length=150),
        ),
    ]
