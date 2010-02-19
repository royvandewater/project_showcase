from django.db import models

class LogEntry(models.Model):
    commit = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField()

    def __unicode__(self):
        return self.description
