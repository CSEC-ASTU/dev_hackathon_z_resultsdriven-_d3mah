# Generated by Django 4.1.5 on 2023-06-10 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_achivement_photo_alter_blog_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=5150)),
            ],
        ),
    ]
