from django.urls import path,include
from . import views
from django.contrib import admin


urlpatterns=[
    path('',views.index,name='uihome'),
    path('ip_check/',views.ip_check,name='uihome'),
    path('wifi/',views.wifi,name='wifi_deauth'),
    path('wifi_deauth/',views.wifi_deauth,name='wifi_deauth'),
    path('mitm/',views.mitm,name='mitm'),
    path('mirai/',views.mirai,name='mirai'),
    path('ns/',views.net,name='net_scan'),
    path('ps/',views.ps,name='port_scan'),
    path('dos/',views.dos,name='dos'),
    path('ripple/',views.ripple,name='ripple'),
]