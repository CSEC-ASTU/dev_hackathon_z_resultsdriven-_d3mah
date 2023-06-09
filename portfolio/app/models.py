from django.db import models

# Create your models here.


class Achivement(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=5150)
    photo = models.ImageField(upload_to="Achivement_img")

    def __str__(self):
        return str(self.title)


class Project(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    description = models.CharField(max_length=5150)
    photo = models.ImageField(upload_to="Project_img")

    def __str__(self):
        return str(self.title)


class Testimonials(models.Model):
    name = models.CharField(max_length=150)
    user_title = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=5150)
    photo = models.ImageField(upload_to="Testimonials_img")

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    date = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=5150)
    photo = models.ImageField(upload_to="Project_img")

    def __str__(self):
        return str(self.title)
