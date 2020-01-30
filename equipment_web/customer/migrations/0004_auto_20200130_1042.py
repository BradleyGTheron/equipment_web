# Generated by Django 2.2.5 on 2020-01-30 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20200129_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='entity_type',
            field=models.CharField(choices=[('SEC', 'Section'), ('DIV', 'Division'), ('DEP', 'Department'), ('BRA', 'Branch'), ('N/A', 'N/A'), ('LAB', 'Lab'), ('HEAD', 'Head Office')], default='SEC', max_length=4, verbose_name='Entity Type'),
        ),
    ]
