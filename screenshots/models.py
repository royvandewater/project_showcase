from django.db import models

# Create your models here.
class Version(models.Model):
    version = models.CharField(max_length=20)
    release_date = models.DateTimeField()

    def __unicode__(self):
        return "v" + self.version

class Screenshot(models.Model):
    title = models.CharField(max_length=100)
    version = models.ForeignKey(Version)
    thumbnail = models.ImageField(upload_to="upload/screenshots/thumb/%Y/%m/%d", help_text="Optimum size is 100x75px")
    full = models.ImageField(upload_to="upload/screenshots/full/%Y/%m/%d")

    def __unicode__(self):
        return self.title
