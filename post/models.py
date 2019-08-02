from django.db import models
from django.utils import timezone
# Create your models here.
class Posts(models.Model):
    title           =       models.CharField(max_length=500)
    description     =       models.CharField(max_length=500)
    content         =       models.TextField()
    author          =       models.CharField(max_length=100)
    date_posted     =       models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
