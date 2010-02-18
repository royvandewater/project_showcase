from django.db import models

# Create your models here.
class Release(models.Model):
    version = models.CharField(max_length=20,unique=True)
    release_date = models.DateTimeField()
    file = models.FileField(upload_to="upload/releases/%Y/%m/%d")
    change_log = models.TextField(null=True,blank=True)

    def __unicode__(self):
        return "v" + self.version

    def filename(self):
        return self.file.url.split("/")[-1]
