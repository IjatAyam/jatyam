from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.urls import reverse

from martor.models import MartorField

from .utils import unique_slug_generator


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    color = models.CharField(max_length=15)
    desc = models.TextField(blank=True)
    order = models.IntegerField(default=1, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    meta_title = models.CharField(max_length=100, blank=True)
    desc = models.TextField(blank=True)
    banner = models.ImageField(upload_to="post/banner/%Y/%m/%d/", blank=True)
    thumb = models.ImageField(upload_to="post/thumb/%Y/%m/%d/", blank=True)
    content = models.TextField()
    meta_tags = models.TextField(blank=True)
    order = models.IntegerField(default=1, blank=True)
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("post_update", kwargs={"pk": self.pk})


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.title, instance.slug)


pre_save.connect(slug_save, sender=Post)
