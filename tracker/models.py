from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class TrackRecord(models.Model):
    tracker_id = models.CharField(primary_key=True,default=uuid.uuid4,max_length=60)
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    email_recipient = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user.username} ({self.email_recipient}) "
    
class VisitHistory(models.Model):
    track = models.ForeignKey(TrackRecord,on_delete=models.CASCADE)
    visit_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.track.__str__().replace(' ','')} - {self.visit_count} visits"

@receiver(post_save,sender=TrackRecord)
def visit_history_creator_signal(sender,instance,**kwargs):
    VisitHistory.objects.create(track=instance)