from django.contrib import admin
from . models import Instrument

class InstrumentAdmin(admin.ModelAdmin):
    exclude= ['date_created','date_updated','created_by','updated_by']
    list_display = ['entity','equipment','serial_number','equipment_card_no','internal_id','is_active']
    search_fields = ('serial_number','equipment','entity')
    list_filter = ('entity','equipment')
    list_per_page = 15


admin.site.register(Instrument, InstrumentAdmin)
