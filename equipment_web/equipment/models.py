from django.db import models
from partner.models import Supplier, Manufacturer
from django.contrib.auth.models import User

class Equipment(models.Model):
    CENTRIFUGE ='CEN'
    SHAKER = 'SHA'
    MIXER = 'MIX'
    ROCKER = 'ROC'
    HOMOGENIZER = 'HOM'
    AUTOCLAVE = 'AUT'
    TEMPERATURE = 'TEMP'
    BALANCE = 'BAL'
    SPECTROPHOTOMETER = 'SPE'
    ELECTROPHORESIS = 'ELE'
    SEQUENCING = 'SEQ'
    MOLECULAR = 'MOL'

    CATEGORY_CHOICES = [
        (CENTRIFUGE, 'Centrifuge'),
        (SHAKER, 'Shaker'),
        (MIXER, 'Mixer'),
        (ROCKER, 'Rocker'),
        (HOMOGENIZER, 'Homogenizer'),
        (AUTOCLAVE, 'Autoclave'),
        (TEMPERATURE, 'Temperature'),
        (BALANCE, 'Balance'),
        (SPECTROPHOTOMETER, 'Spectrophotometer'),
        (ELECTROPHORESIS, 'Electrophoresis'),
        (SEQUENCING, 'Sequencing'),
        (MOLECULAR, 'Molecular'),
    ]
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE,default=0)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,default=0)
    product_name = models.CharField('Name', max_length=100)
    product_code = models.CharField('Code', max_length=20)
    product_description = models.CharField('Description', max_length=250,null=True,blank=True)
    product_note = models.TextField('Note', null=True,blank=True)
    warrenty_period = models.PositiveIntegerField('Warrenty Period (years)',null=True, blank=True,default=0)
    require_calibration = models.BooleanField('Calibration Required',default=False)
    calibration_period = models.PositiveIntegerField('Calibration Period (months)',default=0,
                                                    help_text='Leave set to 0 if the equipment does not require calibration')
    calibration_notes = models.TextField('Calibration Notes', blank=True, null=True)
    category = models.CharField('Category', max_length=4,choices=CATEGORY_CHOICES, default=CENTRIFUGE)
    #image = models.ImageField('Image',upload_to='model_images',null=True,blank=True)
    is_active = models.BooleanField('Is Active',default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50,default='Admin')
    updated_by = models.CharField(max_length=50,default='Admin')

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        # return '{} - {}'.format(self.manufacturer, self.product_name)
        return self.product_name
