from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    fullname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="profile/photo/%Y/%m/%d/")
    no_phone = models.CharField(max_length=20, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    youtube = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
