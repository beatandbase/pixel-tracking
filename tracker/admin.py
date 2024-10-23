from django.contrib import admin
from .models import TrackRecord
from .decode_and_encoder import encode_data


class TrackRecordAdmin(admin.ModelAdmin):
    readonly_fields = ('tracker_link','tracker_id')
    fields = ('tracker_id','email_recipient','user','tracker_link','visit_count')

    list_display = ('email_recipient','user','visit_count')

    def tracker_link(self,*args):
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

admin.site.register(TrackRecord,TrackRecordAdmin)