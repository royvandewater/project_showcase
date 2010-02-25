from django.db import models

# Create your models here.
class Content(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    body = models.TextField(null=True,blank=True,help_text="You can enter html here")

    def __unicode__(self):
        return self.name

class Setting(models.Model):
    name = models.CharField(max_length=255)
    git_key = models.CharField(max_length=255)
    active = models.BooleanField(help_text="One setting must be active at all times, activating this setting deactivates the currently active one")

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.active:
            for setting in Setting.objects.filter(active=True):
                setting.active = False
                setting.save()
        super(Setting, self).save(*args, **kwargs)
