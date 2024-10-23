from django.db import models
from django.contrib.auth import get_user_model
import uuid

class TrackRecord(models.Model):
    tracker_id = models.CharField(primary_key=True,default=uuid.uuid4,max_length=60)
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    email_recipient = models.CharField(max_length=250)
    visitor = models.Model
    visit_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} ({self.email_recipient})"