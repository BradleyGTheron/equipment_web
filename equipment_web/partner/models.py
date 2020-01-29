from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# ------------------------------------------------------------------------------
# SUPPLIERS MODEL - LOCAL SUPPLIER OF THE EQUIPMENT OR PIPETTES
# ------------------------------------------------------------------------------
class Supplier(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    supplier_name = models.CharField('name', max_length=100)
    supplier_code = models.CharField('code', max_length=10,null=True,blank=True)
    supplier_notes = models.TextField('note', max_length=250,null=True,blank=True)
    is_active = models.BooleanField('is active',default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50,default='Admin')
    updated_by = models.CharField(max_length=50,default='Admin')

    class Meta:
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.supplier_name

#-------------------------------------------------------------------------------
# MANNUFACTURER MODEL - THE MANUFACTURER OF THE EQUIPMENT OR PIPETTES
#-------------------------------------------------------------------------------
class Manufacturer(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    manufacturer_name = models.CharField('name', max_length=100)
    manufacturer_code = models.CharField('code', max_length=10,null=True,blank=True)
    manufacturer_note = models.TextField('note', max_length=250,null=True,blank=True)
    is_active = models.BooleanField('is active',default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50,default='Admin')
    updated_by = models.CharField(max_length=50,default='Admin')

    class Meta:
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return self.manufacturer_name
