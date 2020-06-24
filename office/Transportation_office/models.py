from django.db import models

class Cardriver(models.Model):
    driversName=models.CharField(max_length=40)
    phone=models.CharField(max_length=40)
    carType=models.CharField(max_length=40)
    carColor=models.CharField(max_length=40)
    carNumber=models.CharField(max_length=40)
    carStatus=models.CharField(max_length=40)
    def __str__(self):
        return self.driversName

class Transportation(models.Model):
    cardriver_id = models.ForeignKey(Cardriver,on_delete=models.CASCADE)
    nameOf_office=models.CharField(max_length=30)
    officeLocation=models.CharField(max_length=30)
    officePhone=models.CharField(max_length=30)
    TransportFrom=models.CharField(max_length=30)
    TransportTo=models.CharField(max_length=30)
    price=models.CharField(max_length=30)

    def __str__(self):
        return self.nameOf_office
