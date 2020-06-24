from django.shortcuts import render
from django import template
from django.db.models import Count,F,Value
from django.db.models import FilteredRelation
from django.db.models import CharField
from django.db.models.functions import Length,Upper
from django.db.models import Exists
from django.views import generic
from django.http import HttpResponse
from .models import Cardriver
from .models import Transportation
from .form import Cardriver_add
from .form import Transportation1_add
from Transportation_office import form
from Transportation_office import models
from django.db.models import FloatField
from django.db.models import Count
from django.db.models import expressions
from django.db.models import aggregates
register=template.Library()



def transportation12(request):
    transportation12=models.Transportation.objects.all()
    return render(request,'Transportation_office/a.html',{'transporta':transportation12})

def pp(request):
    pg1=models.Cardriver.objects.all()
    return render(request,'Transportation_office/b.html',{'form1':pg1})

def transportation(request): 
    
    tr1=models.Transportation.objects.filter()
    return render(request,'Transportation_office/form1.html',{'transport':tr1})
    

def Datasave(request):
    form1=form.Cardriver_add(request.POST or None)
    msg=''
    if form1.is_valid():
        a=models.Cardriver()
        a.driversName=form1.cleaned_data['driversName']
        a.phone=form1.cleaned_data['phone']
        a.carType=form1.cleaned_data['carType']
        a.carColor=form1.cleaned_data['carColor']
        a.carNumber=form1.cleaned_data['carNumber']
        a.carStatus=form1.cleaned_data['carStatus']
        a.save()
        msg='data is save'

    return render(request,'Transportation_office/form2.html',{'transport2':form1})

def aaa(request):
    b1=form.Transportation1_add(request.POST or None)
    msg=''
    if b1.is_valid():
        b=models.Transportation() 
        b.cardriver_id=b1.cleaned_data['cardriver_id']
        b.nameOf_office=b1.cleaned_data['nameOf_office']
        b.officeLocation=b1.cleaned_data['officeLocation']
        b.officePhone=b1.cleaned_data['officePhone']
        b.TransportFrom=b1.cleaned_data['TransportFrom']
        b.TransportTo=b1.cleaned_data['TransportTo']
        b.price=b1.cleaned_data['price']
        b.save()  
        msg='data is save'            
    return render(request,'Transportation_office/form3.html',{'transport5':b1})
    


