# Generated by Django 3.1.2 on 2020-12-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='RegionalOffice',
            field=models.CharField(choices=[('HARARE', 'harare'), ('RUSAPE', 'rusape'), ('CHINHOI', 'chinhoi'), ('MVURWI', 'mvurwi'), ('BINDURA', 'bindura'), ('KAROI', 'karoi'), ('MUTARE', 'mutare'), ('MARONDERA', 'marondera')], default='harare', max_length=15),
        ),
    ]