from django.db import models

from users.models import ProjectUser

class Comment(models.Model):
    author = models.ForeignKey('users.ProjectUser')
    message = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)
