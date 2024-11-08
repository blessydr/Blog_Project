from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    blog_tag = models.CharField(max_length=30, unique=True) 

    def __str__(self):
        return self.name
    
class Blogs_post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    created_at=models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to="images/")
