# Generated by Django 3.1.2 on 2021-05-13 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asm', '0012_asset_export_to_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='export_to_CSV',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='export_to_PDF',
        ),
    ]
