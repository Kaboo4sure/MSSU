from django.db import models

# Create your models here.
class Visit(models.Model):
    # count = models.IntegerField(default=0)
    page = models.CharField(max_length=255)
    username = models.CharField(max_length=255, default = "anonymous")
    timestamp = models.DateTimeField(auto_now_add=True) # This is used to update datebase to current stamptime when data is added to it.
    
    def __str__(self):
      return f"Visit{self.pk}"
  
  
