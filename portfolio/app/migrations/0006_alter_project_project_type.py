# Generated by Django 4.1.5 on 2023-06-10 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_achivement_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('Web Development', 'Web Development'), ('Python Modules', 'Python Modules'), ('Machine Learning', 'Machine Learning'), ('Publication', 'Publication')], max_length=150),
        ),
    ]
