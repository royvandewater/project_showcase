from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    # Date information
    publish_date = models.DateTimeField()
    # Content
    title = models.CharField(max_length=255) 
    body = models.TextField(null=True, blank=True, help_text="can use html in this field")
    tags = models.ManyToManyField(Tag)
    
    def __unicode__(self):
        return self.title
