# Generated by Django 2.2.5 on 2020-01-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_l2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Building'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_l3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Room Number'),
        ),
    ]
