from django.db import models
from django.utils import timezone

REGIONAL_OFFICE =(
    ('HARARE', 'Harare'),
    ('RUSAPE', 'Rusape' ),
    ('CHINHOI', 'Chinhoi'),
    ('MVURWI', 'Mvurwi'),
    ('BINDURA', 'Bindura'),
    ('KAROI', 'Karoi'),
    ('MUTARE', 'Mutare'),
    ('MARONDERA', 'Marondera'),
)
STATUS_CHOICE =(
    ('WORKING', 'Working'),
    ('NOT FUNCTIONAL' ,'Not functional'),
)

class Asset(models.Model):
    AssetName= models.CharField(max_length=100,null= True)
    SerialNum= models.CharField(max_length=100, blank = True, null= True)
    AssetNum= models.CharField(max_length=100, blank=True, null=True)
    Description= models.CharField(max_length=100,null= True)
    Office= models.CharField(max_length=100,null= True)
    IssuedTo= models.CharField(max_length=100,null= True)
    DatePurch= models.DateField(default=timezone.now,null= True)
    DisposalDate=models.DateField()
    RegionalOffice = models.CharField(max_length=15, choices=REGIONAL_OFFICE, default='Harare')
    Status=models.CharField(max_length=15, choices=STATUS_CHOICE, default='working')
   
    def publish(self):
        self.AssetName()
        self.save()

    def __str__(self):
        return self.Description 

