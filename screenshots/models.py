from django.db import models

# Create your models here.
class Version(models.Model):
    version = models.CharField(max_length=20)

    def __unicode__(self):
        return "v{0}".format(self.version)

class Screenshot(models.Model):
    title = models.CharField(max_length=100)
    version = models.ForeignKey(Version)
    thumbnail = models.ImageField(upload_to="upload/screenshots/thumb/", help_text="Optimum size is 100x75px")
    full = models.ImageField(upload_to="upload/screenshots/full/")

    def __unicode__(self):
        return self.title
