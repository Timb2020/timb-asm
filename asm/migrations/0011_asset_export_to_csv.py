# Generated by Django 3.1.2 on 2021-05-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asm', '0010_auto_20210512_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='export_to_CSV',
            field=models.BooleanField(default=False),
        ),
    ]