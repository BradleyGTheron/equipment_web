# Generated by Django 2.2.5 on 2020-01-23 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Name')),
                ('product_code', models.CharField(max_length=20, verbose_name='Code')),
                ('product_description', models.CharField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('product_note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('warrenty_period', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Warrenty Period (years)')),
                ('require_calibration', models.BooleanField(default=False, verbose_name='Calibration Required')),
                ('calibration_period', models.PositiveIntegerField(default=0, help_text='Leave set to 0 if the equipment does not require calibration', verbose_name='Calibration Period (months)')),
                ('category', models.CharField(choices=[('CEN', 'Centrifuge'), ('SHA', 'Shaker'), ('MIX', 'Mixer'), ('ROC', 'Rocker'), ('HOM', 'Homogenizer'), ('AUT', 'Autoclave'), ('TEMP', 'Temperature'), ('BAL', 'Balance'), ('SPE', 'Spectrophotometer'), ('ELE', 'Electrophoresis'), ('SEQ', 'Sequencing'), ('MOL', 'Molecular')], default='CEN', max_length=4, verbose_name='Category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default='Admin', max_length=50)),
                ('updated_by', models.CharField(default='Admin', max_length=50)),
                ('manufacturer', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='partner.Manufacturer')),
                ('supplier', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='partner.Supplier')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]
