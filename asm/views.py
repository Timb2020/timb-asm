#django imports
from django.shortcuts import render, redirect , get_object_or_404
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponse


#my imports 
#from resources import AssetResource
from tablib import Dataset
from .forms import registerForm,add_assetForm
from .filters import AssetFilter
from .models import Asset
from django.core.mail import send_mail

def notification (request):
    send_mail('hello', 'this is a test email','dmutemachani@timb.co.zw',['dmutemachani@timb.co.zw'], fail_silently=False)
    return(request, 'asm/sent.html')
def home(request):
  Assets=Asset.objects.all()
  Dday=len(Asset.objects.filter(DisposalDate="2020-12-31"))
  context= {'Assets':Assets,"Dday":Dday}
  return render(request, 'asm/home.html',context)

#views for the asset data 
def asset_list(request):
    Assets=Asset.objects.all()
    assetfilter=AssetFilter(request.GET, queryset=Assets)
    Assets=assetfilter.qs
    context= {'Assets':Assets,'assetfilter':assetfilter, }
    return render(request, 'asm/asset_list.html',context)

def due (request):
  Dday=len(Asset.objects.filter(DisposalDate="2020-12-31"))
  Assets=Asset.objects.filter(DisposalDate="2020-12-31")
  context= {"Assets":Assets,"Dday":Dday}
  return render(request, 'asm/due.html',context)

def harare (request):

    assets=Asset.objects.filter(Office="harare")
    context={ 'assets':assets}
    return render(request, 'asm/harare.html' ,context)   


def karoi (request):

    assets=Asset.objects.filter(Office="karoi")
    context={ 'assets':assets}
    return render(request, 'asm/karoi.html' ,context)   


def mvurwi (request):

    assets=Asset.objects.filter(Office="mvurwi")
    context={ 'assets':assets}
    return render(request, 'asm/mvurwi.html' ,context)   

def chinhoi (request):

    assets=Asset.objects.filter(Office="chinhoi")
    context={ 'assets':assets}
    return render(request, 'asm/chinhoi.html' ,context)   

def marondera (request):

    assets=Asset.objects.filter(Office="marondera")
    context={ 'assets':assets}
    return render(request, 'asm/marondera.html' ,context)   

def bindura (request):

    assets=Asset.objects.filter(Office="bindura")
    context={ 'assets':assets}
    return render(request, 'asm/bindura.html' ,context)   

def rusape (request):

    assets=Asset.objects.filter(Office="rusape")
    context={ 'assets':assets}
    return render(request, 'asm/rusape.html' ,context)   
    
def mutare (request):

    assets=Asset.objects.filter(Office="mutare")
    context={ 'assets':assets}
    return render(request, 'asm/mutare.html' ,context)   
    
def office_desks (request):

    assets=Asset.objects.filter(AssetName="office desks")
    context={ 'assets':assets}
    return render(request, 'asm/officedesks.html' ,context)     

def office_chairs (request):

    assets=Asset.objects.filter(AssetName="office chairs")
    context={ 'assets':assets}
    return render(request, 'asm/officechairs.html' ,context)  

def office_cabinets (request):

    assets=Asset.objects.filter(AssetName="office cabinets")
    context={ 'assets':assets}
    return render(request, 'asm/officecabinets.html' ,context)  


def desktops (request):

    assets=Asset.objects.filter(AssetName="monitor")
    context={ 'assets':assets}
    return render(request, 'asm/desktops.html' ,context)  


def mouse (request):

    assets=Asset.objects.filter(AssetName="mouse")
    context={ 'assets':assets}
    return render(request, 'asm/mouse.html' ,context)  

def keyboards (request):

    assets=Asset.objects.filter(AssetName="keyboards")
    context={ 'assets':assets}
    return render(request, 'asm/keyboards.html' ,context)  

def laptops(request):

    assets=Asset.objects.filter(AssetName="")
    context={ 'assets':assets}
    return render(request, 'asm/laptops.html' ,context)      

def office_fan(request):

    assets=Asset.objects.filter(AssetName="office fan")
    context={ 'assets':assets}
    return render(request, 'asm/officefan.html' ,context)           
    
    #adding a new asset
def add_asset(request):
    form = add_assetForm()
    if request.method == "POST":
     form= add_assetForm(request.POST)
    if form.is_valid():
        form.save()
        form= add_assetForm()
        
    context={'form':form}
    return render(request, 'asm/add_asset.html', context)

def edit_asset(request):
    asset = get_object_or_404(Asset)
    form = add_assetForm()
    if request.method == "POST":
     form= add_assetForm(request.POST,instance=asset)
    if form.is_valid():
        form.save()
        form= add_assetForm()
        
    context={'form':form}
    return render(request, 'asm/edit_asset.html', context)

#file upload method


   

#registration page
def register(request):
    form = registerForm()
    if request.method == "POST":
        form=registerForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' +''+ user )
            return redirect('login')
    context={'form':form}
    return render(request, 'asm/reg.html', context)


#login page
def loginPage(request):

    if request.method =="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(request, username= username, password=password)
        if  user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'asm/login.html')


        
    return render(request, 'asm/login.html')

def logOut(request):
        logout(request)
        return redirect('login')

