from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from datetimeutc.fields import DateTimeUTCField
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.conf import settings 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import os
from django.core.validators import RegexValidator

# Create your models here.


def get_upload_path (instance,filename):
    return os.path.join('images','users',str(instance.pk),filename)

class DateTimeUTCField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()





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
    DateTime_UTC= DateTimeUTCField(auto_now=True ,null=True)
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
    




class AccountManager (BaseUserManager):
    def create_user(self ,email,username,password):
        if not email :
            raise ValueError ("Users Must have an email")
        if not username :
            raise ValueError ("Users Must have username")
        user = self.model(
            email=self.normalize_email(email),
            username = username
                          )
        user.set_password(password)
        user.save(using =self._db)
        return user 
    
    def create_superuser(self ,email,username,password):
        
        user = self.create_user(
            email=self.normalize_email(email),
            password =password,
            username = username)
        user.is_admin =True
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using =self._db)
        return user 



class Account (AbstractBaseUser):
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
    phone_regex = RegexValidator(
        regex=r'^\+962\d{8}$'


    )

    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email",max_length=60, unique=True)
    username =models.CharField(max_length=30 ,unique=True)
    Server_DateTime = models.DateTimeField(auto_now_add=True,blank=True ,null=True )
    DateTime_UTC= DateTimeUTCField(auto_now_add=True,null=True)
    date_joined = models.DateTimeField(verbose_name="data_joined" ,auto_now_add=True)
    Update_DateTime_UTC = DateTimeUTCField(auto_now=True)
    status = models.CharField(max_length=15 , choices=USER_STATUS_CHOICES ,default= Active)
    phone = models.CharField(validators=[phone_regex],max_length=15,verbose_name='phone no.',unique=True,blank=True ,null=True )
    gender= models.CharField(max_length=6,choices=[('MALE','Male'),('FEMALE','Female')],blank=True,null=True)
    Date_Of_Birth = models.DateField(blank=True ,null=True ,max_length=8) 
    user_image =models.ImageField(blank=True ,null=True ,upload_to=get_upload_path )
    last_login= DateTimeUTCField(auto_now=True, verbose_name='Last Login',blank =True ,null=True)
    is_admin =models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    claimed_deal =models.ManyToManyField(Deal ,blank=True,null=True)


    USERNAME_FIELD ="username"
    REQUIRED_FIELDS =["email"]

    objects = AccountManager()

    def __str__(self):
        return self.username
    
    def has_perm (self , perm , obj =None):
        return self.is_admin
    
    def has_module_perms (self,app_label):
        return True




# class ClaimedDeal(models.Model):
    
    







@receiver(post_save , sender =settings.AUTH_USER_MODEL)

def create_token (created ,sender , instance   ,**kwargs):
    if created:
        Token.objects.create(user =instance)

    





# class User_Profile (models.Model):
#     Active = "Active"
#     In_Active="In_Active"
#     Deleted = "Deleted"
#     Expired="Expired"

#     USER_STATUS_CHOICES =[
#         (Active ,"Active"),
#         (In_Active,"In Active"),
#         (Deleted ,"Deleted"),
#         (Expired ,"Expired")
#     ]


#     id = models.AutoField(primary_key=True)
#     # user = models.OneToOneField(Account, on_delete=models.CASCADE,null=True ,blank=True ,related_name='profile')
#     Server_DateTime = models.DateTimeField(auto_now_add=True)
#     DateTime_UTC= DateTimeUTCField(null=True)
#     Update_DateTime_UTC = DateTimeUTCField(auto_now=True)
#     last_login = DateTimeUTCField(verbose_name='Last Login',blank =True ,null=True)
#     status = models.CharField(max_length=15 , choices=USER_STATUS_CHOICES ,default= Active)
#     name = models.CharField(max_length=150 ,unique=True)
#     email = models.EmailField(verbose_name='email',blank=True,null=True ,unique=True)
#     phone = PhoneNumberField(verbose_name='phone no.',unique=True)
#     gender= models.CharField(max_length=6,choices=[('MALE','Male'),('FEMALE','Female')],blank=True,null=True)
#     Date_Of_Birth = models.DateField(max_length=8) 
#     user_image =models.ImageField(blank=True ,null=True ,upload_to=get_upload_path )


#     def __str__ (self):
#         return self.name
    



