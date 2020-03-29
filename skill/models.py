from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator


class Skill(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    svg = models.FileField(upload_to="skill/svg/%Y/%m/%d/",
                           validators=[FileExtensionValidator(['svg'])])
    percent = models.IntegerField(
        default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    color = models.CharField(max_length=15)
    order = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return self.title


class Showcase(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    skills = models.ManyToManyField(Skill, related_name="showcases")
    img = models.ImageField(upload_to="showcase/img/%Y/%m/%d/")
    desc = models.TextField(blank=True)
    link_to = models.CharField(max_length=100)
    order = models.IntegerField(default=1, blank=True)
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
