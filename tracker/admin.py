from django.contrib import admin
from .models import TrackRecord,VisitHistory
from .decode_and_encoder import encode_data


class TrackRecordAdmin(admin.ModelAdmin):
    readonly_fields = ('tracker_link',)
    fields = ('tracker_id','email_recipient','user','tracker_link')

    list_display = ('tracker_id','email_recipient','user')

    def tracker_link(self,*args):
        import base64
        import json
        is_formatted = False

        data = {
            "user":args[0].user.get_username(),
            "tracker_id":args[0].pk,
        }

        encoded = encode_data(data)

        params = f"/image/?params={encoded}"
        if is_formatted:
            from django.utils.html  import format_html
            return format_html('<a  href="{}" target="_blank">Tracker Link</a>', params)
        else:
            from django.conf import settings
            return f'{settings.DOMAIN_NAME}{params}'
    
    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change) 
    #     if not change:
    #         self.message_user(request,'Use your Uuid to track param for image.')

admin.site.register(TrackRecord,TrackRecordAdmin)
admin.site.register(VisitHistory)