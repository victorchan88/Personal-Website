from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField(null=True)
    body = models.TextField()
    thumb = models.ImageField(default='default.jpg', blank=True)
    full = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title
