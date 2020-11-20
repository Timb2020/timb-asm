from django.urls  import path
from .import views 

urlpatterns =[
    path('', views.asset_list, name='asset_list'),
    path('Asset/new', views.add_asset, name='add_asset'),
    path('register',views.register, name='register' ),
    path('login', views.loginPage, name=''),
    path('loginout', views.logOut, name='logOut'),
]