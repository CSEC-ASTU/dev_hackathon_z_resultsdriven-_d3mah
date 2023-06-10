# Generated by Django 4.1.5 on 2023-06-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_achivement_photo_alter_blog_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivement',
            name='photo',
            field=models.ImageField(blank=True, default='index.jpg', upload_to='Achivement_img'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, default='index.jpg', upload_to='Project_img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, default='index.jpg', upload_to='Project_img'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='photo',
            field=models.ImageField(blank=True, default='index.jpg', upload_to='Testimonials_img'),
        ),
    ]
