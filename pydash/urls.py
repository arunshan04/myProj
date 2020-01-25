from django.urls import path
from . import views

urlpatterns = [path('index', views.index, name='index'),
               path('login/', views.myLogin,name='login'),
               path('logout/', views.myLogout, name='logout'),
               path('info/uptime/', views.uptime, name='uptime'),
               path('info/memory/', views.memusage, name='memusage'),
               path('info/cpuusage/', views.cpuusage, name='cpuusage'),
               path('info/getdisk/', views.getdisk, name='getdisk'),
               path('info/getusers/', views.getusers, name='getusers'),
               path('info/getips/', views.getips, name='getips'),
               path('info/gettraffic/', views.gettraffic, name='gettraffic'),
               path('info/proc/', views.getproc, name='getproc'),
               path('info/getdiskio/', views.getdiskio, name='getdiskio'),
               path('info/loadaverage/', views.loadaverage, name='loadaverage'),
               path('info/platform/([\w\-\.]+)/', views.platform, name='platform'),
               path('info/getcpus/([\w\-\.]+)/', views.getcpus, name='getcpus'),
               path('info/getnetstat/', views.getnetstat, name='getnetstat')
               ]
