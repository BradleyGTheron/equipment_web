from django.contrib import admin
from . models import Instrument
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter, RelatedDropdownFilter

class InstrumentAdmin(admin.ModelAdmin):
    exclude= ['date_created','date_updated','created_by','updated_by']
    list_display = ['serial_number','equipment','entity','is_active']
    search_fields = ('serial_number','equipment','entity')
    #list_filter = ('equipment','entity')
    list_filter = (('equipment', RelatedDropdownFilter),
        (('entity', RelatedDropdownFilter)),

    )
    list_per_page = 15
    ordering = ('equipment','entity')


admin.site.register(Instrument, InstrumentAdmin)
