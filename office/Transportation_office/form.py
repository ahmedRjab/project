from django import forms
from .models import Cardriver
from .models import Transportation

class Cardriver_add(forms.Form):
    driversName=forms.CharField(required=True , widget=forms.TextInput())
    phone=forms.CharField(required=True , widget=forms.TextInput())
    carType=forms.CharField(required=True , widget=forms.TextInput())
    carColor=forms.CharField(required=True , widget=forms.TextInput())
    carNumber=forms.CharField(required=True , widget=forms.TextInput())
    carStatus=forms.CharField(required=True , widget=forms.TextInput())

    class Meta:
        model=Cardriver
        fields=['driversName','phone','carType','carColor','carNumber','carStatus']
        labels={
           
            'driversName': 'اسم السائق',
            'phone': 'التلفون',
            'carType': 'نوع السيارة',
            'carColor': 'لون السيارة',
            'carNumber': 'رقم السيارة',
            'carStatus': 'حالة السيارة',
        }

class Transportation_add(forms.Form):
   
    cardriver_id =forms.CharField(required=True , widget=forms.TextInput())
    nameOf_office=forms.CharField(required=True , widget=forms.TextInput())
    officeLocation=forms.CharField(required=True , widget=forms.TextInput())
    officePhone=forms.CharField(required=True , widget=forms.TextInput())
    TransportFrom=forms.CharField(required=True , widget=forms.TextInput())
    TransportTo=forms.CharField(required=True , widget=forms.TextInput())
    price=forms.CharField(required=True , widget=forms.TextInput())

    class Meta:
        model=Transportation
        fields=['nameOf_office','officeLocation','officePhone','TransportFrom','TransportTo','price']
        labels={
           
            'nameOf_office': 'اسم المكتب',
            'officeLocation': 'الموقع',
            'officePhone': 'تلفون المكتب',
            'TransportFrom': 'من',
            'TransportTo': 'إلى',
            'price': 'السعر',
        }

class Transportation1_add(forms.ModelForm):
    class Meta:
        model=Transportation
        fields=['cardriver_id','nameOf_office','officeLocation','officePhone','TransportFrom','TransportTo','price']
        cardriver_id=forms.CharField(required=True , widget=forms.TextInput())
        nameOf_office=forms.CharField(required=True , widget=forms.TextInput())
        officeLocation=forms.CharField(required=True , widget=forms.TextInput())
        officePhone=forms.CharField(required=True , widget=forms.TextInput())
        TransportFrom=forms.CharField(required=True , widget=forms.TextInput())
        TransportTo=forms.CharField(required=True , widget=forms.TextInput())
        price=forms.CharField(required=True , widget=forms.TextInput())    


    


       


    