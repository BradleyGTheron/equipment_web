from django.contrib import admin
from . models import Equipment
from partner.models import Manufacturer
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter, RelatedDropdownFilter

# INSTRUMENT ADMIN.PY

class EquipmentAdmin(admin.ModelAdmin):
    exclude= ['date_created','date_updated','created_by','updated_by']
    list_display = ['product_name','manufacturer','product_code','category','is_active']
    search_fields = ('cat_no',)
    list_filter = (('manufacturer', RelatedDropdownFilter),
        ('category', ChoiceDropdownFilter),
    )
    list_per_page = 15
    ordering = ('manufacturer','category')
#    fields = (('manufacturer','supplier'),'product_name','product_code','product_note',
#            'image','is_active')

    fieldsets = (
        (None, {
            'fields':(('manufacturer','supplier'),'product_name','product_code','category','product_note',
                    'image','is_active',),
        }),
        ('Service Options', {
            'fields':('warrenty_period',('require_calibration','calibration_period'),),
        }),
    )

admin.site.register(Equipment, EquipmentAdmin)
