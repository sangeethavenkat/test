from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admins/', admin.site.urls),
    path('',include('admins.urls')),
    path('pm/',include('projectmanager.urls')),
    path('tl/',include('teamleader.urls')),
    path('emp/',include('employee.urls')),
]
