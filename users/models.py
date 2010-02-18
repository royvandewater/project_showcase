from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProjectUser(models.Model):
    user = models.ForeignKey(User, unique=True)
    reset_string = models.CharField(max_length=255,null=True,blank=True)

    def __unicode__(self):
        return "%s (%s)" % (self.user.username, self.user.get_full_name())
