import django_filters
from .models import Asset
from django_filters import DateFilter, CharFilter
from django import forms

class AssetFilter(django_filters.FilterSet):
  
    asset=CharFilter(field_name='AssetName', lookup_expr="icontains")
    class Meta:
        model = Asset
        fields= '__all__'
        exclude =['DatePurch','SerialNum', 'AssetNum','AssetName','Office','IssuedTo','DisposalDate','export_to_PDF','export_to_CSV']
 
class ReportFilter(django_filters.FilterSet):
    class Meta:
        model = Asset
        fields=['AssetName','Description','RegionalOffice','Status', 'DatePurch', 'DisposalDate']
        
