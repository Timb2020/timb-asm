import django_filters
from .models import Asset
from django_filters import DateFilter, CharFilter

class AssetFilter(django_filters.FilterSet):
    Date= DateFilter(field_name="DisposalDate", lookup_expr='gte')
    asset=CharFilter(field_name='AssetName', lookup_expr="icontains")
    class Meta:
        model = Asset
        fields= '__all__'
        exclude =['DatePurch','SerialNum', 'AssetNum','AssetName','Office','IssuedTo','DisposalDate']
