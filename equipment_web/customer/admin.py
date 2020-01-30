from django.contrib import admin
from . models import Account, Entity, Address
from instrument.models import Instrument
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

class EntityInLine(admin.TabularInline):
    model = Entity
    fields = ('entity_name','entity_abbreviation','entity_type','is_active')
    #readonly_fields = ('entity_name','entity_abbreviation','entity_type',)
    show_change_link = True
    extra = 0

class InstrumentInLine(admin.TabularInline):
    model = Instrument
    fields = ('serial_number','equipment','is_active')
    show_change_link = True
    extra = 0

class AccountAdmin(admin.ModelAdmin):
    exclude= ['date_created','date_updated','created_by','updated_by']
    list_display = ['account_name','account_code','internal_code','is_active']
    search_fields = ('account_name',)
    inlines = (EntityInLine,)
    list_per_page = 15

class EntityAdmin(admin.ModelAdmin):
    exclude= ['date_created','date_updated','created_by','updated_by']
    list_display = ['entity_name','account','entity_type','is_active']
    search_fields = ('entity_name',)
    list_filter = (
        ('account', RelatedDropdownFilter),
    )
    inlines = (InstrumentInLine,)
    list_per_page = 15

class AddressAdmin(admin.ModelAdmin):
    exclude= ['date_created','date_updated','created_by','updated_by']
    list_display = ['entity','address_type','is_active']

admin.site.register(Account, AccountAdmin)
admin.site.register(Entity, EntityAdmin)
admin.site.register(Address, AddressAdmin)
