from django.db import models

# Create your models here.
class Release(models.Model):
    version = models.CharField(max_length=20)
    release_date = models.DateTimeField()
    file = models.FileField(upload_to="upload/releases/")
    change_log = models.TextField(null=True,blank=True)

    def __unicode__(self):
        return "v{0}".format(self.version)