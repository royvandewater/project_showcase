from django.db import models
from django.contrib.auth.models import User

class ProjectUser(models.Model):
    user = models.ForeignKey(User, unique=True)
    reset_string = models.CharField(max_length=255,null=True,blank=True)

    def __unicode__(self):
        return "%s (%s)" % (self.user.username, self.user.get_full_name())

    def build_user(self, username, first_name, last_name, email):
        user = User()
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        self.user = user
