# Generated by Django 3.1.2 on 2021-05-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asm', '0011_asset_export_to_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='export_to_PDF',
            field=models.BooleanField(default=False),
        ),
    ]
