# Generated by Django 3.1.2 on 2021-05-11 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asm', '0006_asset_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='user',
            new_name='owner',
        ),
    ]
