from django.db import models

# Create your models here.
class Visits(models.Model):
    count = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Visits"
