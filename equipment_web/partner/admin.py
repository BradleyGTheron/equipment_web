from django.contrib import admin
from . models import Supplier, Manufacturer
from equipment.models import Equipment

class EquipmentInline(admin.TabularInline):
    model = Equipment
    fields = ('product_name','product_code','is_active',)
    readonly_fields = ('product_name','product_code','is_active',)
    show_change_link = True
    extra = 0

class SupplierAdmin(admin.ModelAdmin):
    exclude = ['date_created','date_updated','created_by','updated_by']
    list_display = ('supplier_name','supplier_code','is_active')
    fields = ('supplier_name','supplier_code','supplier_notes','image','is_active')

# MANUFACTURER MODEL REGISTER
class ManufacturerAdmin(admin.ModelAdmin):
    exclude = ['date_created','date_updated','created_by','updated_by']
    list_display = ('manufacturer_name','manufacturer_code','is_active')
    fields = ('manufacturer_name','manufacturer_code','manufacturer_note','image','is_active')
    inlines = (EquipmentInline,)

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
