from django.contrib import admin
from .models import Asset
from import_export.admin import ImportExportModelAdmin


@admin.register(Asset)
class AssetAdmin(ImportExportModelAdmin):
    list_display =('AssetName','SerialNum', 'AssetNum', 'Description','Office', 'IssuedTo', 'DatePurch','DisposalDate')