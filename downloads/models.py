from django.db import models

import re

# Create your models here.
class Release(models.Model):
    version = models.CharField(max_length=20,unique=True)
    release_date = models.DateTimeField()
    file = models.FileField(upload_to="upload/releases/%Y/%m/%d", null=True, blank=True)
    display_name = models.CharField(max_length=255, help_text="Leave blank to use filename", null=True, blank=True)
    change_log = models.TextField(null=True,blank=True, help_text="You can enter html in this field")

    def __unicode__(self):
        return self.version

    def filename(self):
        if self.display_name:
            return self.display_name
        else:
            return self.download_name()

    def download_name(self):
        filename = self.file.url.split("/")[-1]
        underscore = re.compile('_+\.')
        return underscore.sub('.', filename)
