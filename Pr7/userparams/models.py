from django.db import models

# Create your models here.


class Myblog(models.Model):
    title = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)
    bigdesc = models.CharField(max_length=400)
