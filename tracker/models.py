from django.db import models
from django.contrib.auth import get_user_model
import uuid

class TrackRecord(models.Model):
    tracker_id = models.CharField(primary_key=True,default=uuid.uuid4,max_length=60)
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True, blank=True)
    email_recipient = models.CharField(max_length=250)
    visit_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} ({self.email_recipient})"
    
class VisitorRecord(models.Model):
    ip = models.GenericIPAddressField(null=True, blank=True)
    isp = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=200,null=True, blank=True)
    state = models.CharField(max_length=50,null=True, blank=True)
    country = models.CharField(max_length=50,null=True, blank=True)
    user_agent = models.CharField(max_length=100,null=True, blank=True)
    track  = models.ForeignKey(TrackRecord,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"{str(self.track)}- {self.user_agent[:12]}..."