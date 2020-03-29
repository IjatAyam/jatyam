from django.db import models


class HomeSlider(models.Model):
    ALIGN_CHOICES = [
        ('left', 'left'),
        ('center', 'center'),
        ('right', 'right'),
    ]

    name = models.CharField(max_length=50)
    banner = models.ImageField(upload_to="home/slider/banner/%Y/%m/%d/")
    title = models.CharField(max_length=100, blank=True)
    desc = models.TextField(blank=True)
    button_label = models.CharField(max_length=50, blank=True)
    button_to = models.CharField(max_length=75, blank=True)
    align = models.CharField(
        max_length=10,
        choices=ALIGN_CHOICES,
        default='left',
    )
    order = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return self.name
