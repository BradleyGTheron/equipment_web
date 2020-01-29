# Generated by Django 2.2.5 on 2020-01-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=100, verbose_name='name')),
                ('manufacturer_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='code')),
                ('manufacturer_note', models.TextField(blank=True, max_length=250, null=True, verbose_name='note')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default='Admin', max_length=50)),
                ('updated_by', models.CharField(default='Admin', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100, verbose_name='name')),
                ('supplier_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='code')),
                ('supplier_notes', models.TextField(blank=True, max_length=250, null=True, verbose_name='note')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default='Admin', max_length=50)),
                ('updated_by', models.CharField(default='Admin', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Suppliers',
            },
        ),
    ]