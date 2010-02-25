from django.db import models

class Commit(models.Model):
    commit = models.CharField(max_length=255)
    commit_url = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255)
    message = models.TextField()
    datetime = models.DateTimeField()

    def __unicode__(self):
        return self.message
