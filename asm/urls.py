from django.urls  import path
from .import views 

urlpatterns =[
    path('index',views.home, name='home'),
    path('Assets', views.asset_list, name='asset_list'),
    path('Asset/new', views.add_asset, name='add_asset'),
    path('register',views.register, name='register' ),
    path('', views.loginPage, name='login'),
    path('loginout', views.logOut, name='logOut'),
    path('Assets/Harare',views.harare, name='harare'),
    path('Assets/Karoi',views.karoi, name='karoi'),
    path('Assets/Mvurwi',views.mvurwi, name='mvurwi'),
    path('Assets/Mutare',views.mutare, name='mutare'),
    path('Assets/Marondera',views.marondera, name='marondera'),
    path('Assets/Chinhoi',views.chinhoi, name='chinhoi'),
    path('Assets/Rusape',views.rusape, name='rusape'),
    path('Assets/Bindura',views.bindura, name='bindura'),
    path('Assets/office_desks', views.office_desks, name='office_desks'),
    path('Assets/office_chairs', views.office_chairs, name='office_chairs'),
    path('Assets/office_fan', views.office_fan, name='office_fan'),
    path('Assets/office_cabinets', views.office_cabinets, name='office_cabinets'),
    path('Assets/desktops', views.desktops, name='desktops'),
    path('Assets/mouse', views.mouse, name='mouse'),
    path('Assets/keyboards', views.keyboards, name='keyboards'),
    path('Assets/laptops', views.laptops, name='laptops'),
    path('Assets/Due', views.due, name='due'),
    path('sent', views.notification, name='sent'),
    path('Asset/edit', views.edit_asset, name='edit'),

   

]