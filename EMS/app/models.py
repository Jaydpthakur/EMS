from django.db import models

# Create your models here.

class UserData(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    mobile=models.IntegerField()
    password=models.CharField( max_length=50)
    cpassword=models.CharField( max_length=50)
    
    def __str__(self) -> str:
        return str(self.name)
    
class AdminDataBase(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Contact=models.IntegerField()
    Password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Firstname
    
class EnquiryDataBase(models.Model):
    Studentname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Contact=models.IntegerField()
    Enquiry=models.TextField()
    def __str__(self):
        return self.Studentname
