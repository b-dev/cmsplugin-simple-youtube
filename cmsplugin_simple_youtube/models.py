from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _
import settings

class SimpleYouTube(models.Model):
    name = models.CharField(_('name'), max_length=255, blank=False, null=False)
    video_id = models.CharField(_('video id'), max_length=60)
    autoplay = models.BooleanField(_('autoplay'),default=settings.CMS_SIMPLEYOUTUBE_AUTOPLAY)
    custom_thumbnail = models.ImageField(upload_to='youtube_th', blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name,)

    def video_url(self):
        return u'http://www.youtube.com/watch?v=%s' % self.video_id

    def thumbnail(self):
        return u'<img src="http://i4.ytimg.com/vi/%s/default.jpg" />' % self.video_id
    thumbnail.allow_tags = True


class SimpleYoutubePointer(CMSPlugin):
    youtube = models.ForeignKey(SimpleYouTube)
    class Meta:
        verbose_name = _("SimpleYoutube")

    def __unicode__(self):
        return self.youtube.name
