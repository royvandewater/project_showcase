from django.db import models

# Create your models here.
class Screenshot(models.Model):
    title = models.CharField(max_length=100)
    version = models.IntegerField()
    thumbnail = models.ImageField(upload_to="upload/screenshots/thumb/")
    full = models.ImageField(upload_to="upload/screenshots/full/")

    def __unicode__(self):
        return self.title
