# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.home, name='home'),
    path('api/', include('myapp.urls')),
]
