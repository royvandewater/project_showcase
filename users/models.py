from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProjectUser(models.Model):
    user = models.ForeignKey(User, unique=True)
    reset_string = models.CharField(max_length=32,null=True,blank=True)

    def __unicode__(self):
        return "{0} ({1})".format(self.user.username, self.user.get_full_name())
