# Generated by Django 4.1.5 on 2023-06-10 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_achivement_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Project_img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Project_img'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='photo',
            field=models.ImageField(blank=True, default=1, upload_to='Testimonials_img'),
            preserve_default=False,
        ),
    ]
