from django.db import models


# Create your models here.
class Session(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    actor = models.CharField(max_length=100)

