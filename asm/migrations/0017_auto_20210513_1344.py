# Generated by Django 3.1.2 on 2021-05-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asm', '0016_auto_20210513_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='owner',
        ),
        migrations.AddField(
            model_name='asset',
            name='export_to_CSV',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='asset',
            name='export_to_PDF',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='asset',
            name='RegionalOffice',
            field=models.CharField(blank=True, choices=[('HARARE', 'Harare'), ('RUSAPE', 'Rusape'), ('CHINHOI', 'Chinhoi'), ('MVURWI', 'Mvurwi'), ('BINDURA', 'Bindura'), ('KAROI', 'Karoi'), ('MUTARE', 'Mutare'), ('MARONDERA', 'Marondera')], default='Harare', max_length=15),
        ),
    ]
