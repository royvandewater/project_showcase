from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    # Date information
    creation_date = models.DateTimeField()
    publish_date = models.DateTimeField()
    # Content
    title = models.CharField(max_length=255) 
    body = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    
