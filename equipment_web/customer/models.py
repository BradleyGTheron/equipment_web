from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    account_name = models.CharField('Account Name', max_length=100)
    account_code = models.CharField('Account Code', max_length=10,null=True,blank=True)
    internal_code = models.CharField('Internal Code', max_length=10,null=True,blank=True)
    is_active = models.BooleanField('Is Active',default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50,default='Admin')
    updated_by = models.CharField(max_length=50,default='Admin')

    class Meta:
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.account_name


class Entity(models.Model):
    SECTION = 'SEC'
    DIVISION = 'DIV'
    DEPARTMENT ='DEP'
    BRANCH = 'BRA'

    TYPE_CHOICES = [
        (SECTION, 'Section'),
        (DIVISION, 'Division'),
        (DEPARTMENT, 'Department'),
        (BRANCH, 'Branch'),
    ]

    entity_name = models.CharField('Entity Name',max_length=100)
    entity_abbreviation = models.CharField('Abbreviation',max_length=15,null=True,blank=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE,default=0)
    entity_type = models.CharField('Entity Type', max_length=4,choices=TYPE_CHOICES, default=SECTION)
    is_active = models.BooleanField('Is Active',default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50,default='Admin')
    updated_by = models.CharField(max_length=50,default='Admin')

    class Meta:
        verbose_name_plural = 'Entaties'

    def __str__(self):
        #return '{} - ({})'.format(self.account, self.entity_name)
        return self.entity_name

class Address(models.Model):
    EASTERN_CAPE = 'EC'
    FREE_STATE = 'FS'
    GAUTENG = 'GT'
    KWAZULU_NATAL = 'NL'
    LIMPOPO = 'LP'
    MPUMALANGA = 'MP'
    NORTHERN_CAPE = 'NC'
    NORTH_WEST = 'NW'
    WESTERN_CAPE ='WC'

    PROVINCE_CHOICES = [
        (EASTERN_CAPE, 'Easter Cape'),
        (FREE_STATE, 'Free State'),
        (GAUTENG, 'Gauteng'),
        (KWAZULU_NATAL,  'Kwazulu-Natal'),
        (LIMPOPO,  'Limpopo'),
        (MPUMALANGA, 'Mpumalanga'),
        (NORTHERN_CAPE, 'Northern Cape'),
        (NORTH_WEST, 'North West'),
        (WESTERN_CAPE, 'Western Cape'),
    ]

    POSTAL = 'PS'
    BILLING = 'BL'
    PHYSICAL = 'PY'
    COLLECTION = 'CL'
    DELIVERY = 'CL'
    COLLECTION_DELIVERY = 'CD'

    TYPE_CHOICES = [
        (POSTAL, 'Postall'),
        (BILLING, 'Billing'),
        (PHYSICAL, 'Physical'),
        (COLLECTION, 'Collection'),
        (DELIVERY, 'Delivery'),
        (COLLECTION_DELIVERY, 'Collection/Delivery')
    ]

    entity = models.ForeignKey(Entity,on_delete=models.CASCADE,default=0)
    address_type = models.CharField('Address Type', max_length=4,choices=TYPE_CHOICES, default=PHYSICAL)
    address_l1 = models.CharField('Street Address',max_length=100)
    address_l2 = models.CharField('Building',max_length=100, null=True, blank=True)
    address_l3 = models.CharField('Room Number',max_length=100, null=True, blank=True)
    suburb = models.CharField('Suburb',max_length=50)
    city = models.CharField('City',max_length=50)
    province = models.CharField('Province', max_length=4,choices=PROVINCE_CHOICES, default=GAUTENG)
    code = models.CharField('Code',max_length=4)
    is_active = models.BooleanField('Is Active',default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50,default='Admin')
    updated_by = models.CharField(max_length=50,default='Admin')

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        #return '{} - ({})'.format(self.entity.account, self.entity)
        return self.entity.entity_name
