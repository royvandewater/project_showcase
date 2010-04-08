from django.db import models
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

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
    git_key = models.CharField(max_length=255, help_text="Must be an alphanumeric string, no spaces or symbols. Your github key can be used for github's post-receive hooks. The url is in the form of http://yoursite.com/log/github/gitkey/<replace_with_your_key>/")
    active = models.BooleanField(help_text="One setting must be active at all times, activating this setting deactivates the currently active one")
    theme = models.CharField(max_length=255, help_text="Place jquery-ui theme in MEDIA_PATH/themes/ and enter theme name here")

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.active:
            for setting in Setting.objects.filter(active=True):
                setting.active = False
                setting.save()
        super(Setting, self).save(*args, **kwargs)

    def github_url(self):
        kwargs = {'git_key': self.git_key}
        current_site = Site.objects.get_current()
        return "http://" + current_site.domain + reverse("dev_log.views.github", kwargs=kwargs)
