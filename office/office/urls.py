from django.contrib import admin
from django.urls import path
from Transportation_office import views
from Transportation_office import models




urlpatterns = [
    path('admin/', admin.site.urls),
    path('transportation12/', views.transportation12 , name='transportation12'),
    path('a12/', views.pp , name='cardrivers1'),
    path('transporta/', views.transportation , name='transporta'),
    path('form2/', views.Datasave , name='form2'),   
    path('aaa/', views.aaa , name='aaa'),
    
]