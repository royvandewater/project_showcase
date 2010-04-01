from django.db import models
from django.contrib import comments

from users.models import ProjectUser

class Status(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey('users.ProjectUser')
    created_date = models.DateField(auto_now=True)
    message = models.TextField()

class Ticket(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey('users.ProjectUser')
    status = models.ForeignKey('tickets.Status')
    description = models.TextField()
    open_date = models.DateField(auto_now=True)
    close_date = models.DateField(blank=True, null=True)
    priority = models.IntegerField()
    comments = models.ManyToManyField(Comment)

    def __unicode__(self):
        return self.name

