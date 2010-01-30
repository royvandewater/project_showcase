from django.db import models

# Create your models here.
class Content(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    body = models.TextField(null=True,blank=True)

    def __unicode__(self):
        return self.title
