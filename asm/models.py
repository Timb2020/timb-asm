from django.db import models
from django.utils import timezone

class Asset(models.Model):
    AssetName= models.CharField(max_length=100)
    SerialNum= models.CharField(max_length=100, blank = True, null= True)
    AssetNum= models.CharField(max_length=100, blank=True, null=True)
    Description= models.CharField(max_length=100)
    Office= models.CharField(max_length=100)
    IssuedTo= models.CharField(max_length=100)
    DatePurch= models.DateField(default=timezone.now)
    DisposalDate=models.DateField()

    def publish(self):
        self.AssetName()
        self.save()

    def __str__(self):
        return self.Description 

