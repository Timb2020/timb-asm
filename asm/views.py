from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout

from .forms import registerForm,add_assetForm
from .filters import AssetFilter
from .models import Asset

def asset_list(request):
    Assets=Asset.objects.all()
    Dday=len(Asset.objects.filter(DisposalDate="2020-12-31"))
    assetfilter=AssetFilter(request.GET, queryset=Assets)
    Assets=assetfilter.qs
    context= {'Assets':Assets,'assetfilter':assetfilter, "Dday":Dday}
    return render(request, 'asm/asset_list.html',context)



def add_asset(request):
    form = add_assetForm()
    if request.method == "POST":
     form= add_assetForm(request.POST)
    if form.is_valid():
        form.save()
        form= add_assetForm()
        
    context={'form':form}
    return render(request, 'asm/add_asset.html', context)

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

def loginPage(request):

    if request.method =="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(request, username= username, password=password)
        if  user is not None:
            login(request, user)
            return redirect('asset_list')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'asm/login.html')


        
    return render(request, 'asm/login.html')

def logOut(request):
        logout(request)
        return redirect('login')

