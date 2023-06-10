from django.db import models

# Create your models here.
types = (
    ('Web Development', 'Web Development'),
    ('Modules', 'Modules'),
    ('Machine Learning', 'Machine Learning'),
    ('Publication', 'Publication'),
)


class Achivement(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=5150)
    photo = models.ImageField(
        default="index.jpg", blank=True, upload_to="Achivement_img")

    def __str__(self):
        return str(self.title)


class Project(models.Model):
    project_type = models.CharField(max_length=150, choices=types)
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    description = models.CharField(max_length=5150)
    photo = models.ImageField(
        default="index.jpg", blank=True, upload_to="Project_img")

    def __str__(self):
        return str(self.title)


class Testimonials(models.Model):
    name = models.CharField(max_length=150)
    user_title = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=5150)
    photo = models.ImageField(
        default="index.jpg", blank=True, upload_to="Testimonials_img")

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    date = models.CharField(max_length=150)
    length = models.CharField(blank=True, max_length=150)
    url = models.CharField(blank=True, max_length=150)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=5150)
    photo = models.ImageField(
        default="index.jpg", blank=True, upload_to="Project_img")

    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    phone = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    message = models.CharField(max_length=5150)

    def __str__(self):
        return str(self.name)


class Stats(models.Model):
    rank = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=150, blank=True, default="Mukerem Ali")
    site = models.CharField(max_length=50, blank=True)
    score = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.site)
