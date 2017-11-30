from django.db import models

# Create your models here.
class News(models.Model):
    href = models.CharField(max_length=100, default='', unique=True)
    title = models.CharField(max_length=100, blank=True, default='')
    datetime = models.DateTimeField()
    content = models.CharField(max_length=1024, default='') 
    coverimg = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('-datetime',)

