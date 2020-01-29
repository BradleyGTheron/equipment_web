from django.db import models
from equipment.models import Equipment
from customer.models import Entity

# Create your models here.
class Instrument(models.Model):
    entity = models.ForeignKey(Entity,on_delete=models.CASCADE,default=0)
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE,default=0)
    serial_number = models.CharField('Serial Number', max_length=20)
    internal_id = models.CharField('Tag Number',max_length=20,null=True,blank=True)
    equipment_card_no = models.CharField('Equipment Card # (SAP)',max_length=5, null=True,blank=True)
    date_installed = models.DateField('Data Installed',null=True,blank=True)
    is_active = models.BooleanField('Is Active',default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50,default='Admin')
    updated_by = models.CharField(max_length=50,default='Admin')

    class Meta:
        verbose_name_plural = 'Instruments'

    def __str__(self):
        return '{} - {}'.format(self.entity, self.equipment)
