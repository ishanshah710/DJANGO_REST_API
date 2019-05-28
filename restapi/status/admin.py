from django.contrib import admin
from status.models import Status

from status.forms import StatusForm

class StatusAdmin(admin.ModelAdmin):
    list_display = [ 'pk','user','__str__' ,'image']
    # class Meta:
    #     model = Status
    form = StatusForm

admin.site.register(Status , StatusAdmin)
