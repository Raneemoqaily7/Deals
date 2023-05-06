from django.db import models

from datetimeutc.fields import DateTimeUTCField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import os

# Create your models here.


def get_upload_path (instance,filename):
    return os.path.join('images','users',str(instance.pk),filename)
class User_Profile (models.Model):
    Active = "Active"
    In_Active="In_Active"
    Deleted = "Deleted"
    Expired="Expired"

    USER_STATUS_CHOICES =[
        (Active ,"Active"),
        (In_Active,"In Active"),
        (Deleted ,"Deleted"),
        (Expired ,"Expired")
    ]


    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null =True ,blank=True)
    Server_DateTime = models.DateTimeField(auto_now_add=True)
    DateTime_UTC= DateTimeUTCField(null=True)
    Update_DateTime_UTC = DateTimeUTCField(auto_now=True)
    last_login = DateTimeUTCField(verbose_name='Last Login',blank =True ,null=True)
    status = models.CharField(max_length=15 , choices=USER_STATUS_CHOICES ,default= Active)
    name = models.CharField(max_length=150 ,unique=True)
    email = models.EmailField(verbose_name='email',blank=True,null=True ,unique=True)
    phone = PhoneNumberField(verbose_name='phone no.',unique=True)
    gender= models.CharField(max_length=6,choices=[('MALE','Male'),('FEMALE','Female')],blank=True,null=True)
    Date_Of_Birth = models.DateField(max_length=8) 
    user_image =models.ImageField(blank=True ,null=True ,upload_to=get_upload_path )


    def __str__ (self):
        return self.name
    





class Deal (models.Model):

    Active = "Active"
    In_Active="In_Active"
    Deleted = "Deleted"
    Expired="Expired"


    DEAL_STATUS_CHOICES =[
        (Active ,"Active"),
        (In_Active,"In Active"),
        (Deleted ,"Deleted"),
        (Expired ,"Expired")
    ]


    id = models.AutoField(primary_key=True)
    Server_DateTime =models.DateTimeField(auto_now_add=True)
    DateTime_UTC= DateTimeUTCField(null=True)
    Update_DateTime_UTC = DateTimeUTCField(auto_now=True)
    name = models.CharField(max_length=150 ,unique=True)
    Description = models.TextField(default="No Description")
    status = models.CharField(max_length=10 , choices=DEAL_STATUS_CHOICES ,default= Active)
    amount = models.DecimalField(
        max_digits=9, decimal_places=3
    )
    currency = models.CharField(max_length=6, default=" USD")

    def __str__(self):
        return self.name
    