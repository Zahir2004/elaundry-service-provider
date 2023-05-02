from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from datetime import datetime

# Create your models here.

class demo(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
# above is for demonstration


# making a custom user
class MyHolderManager(BaseUserManager):
    def create_user(self, email, username, phone, role, password=None):
        if not email:
            raise ValueError("User must have email address")
        if not username:
            raise ValueError("User must have username")
        if not phone:
            raise ValueError("User must have phone")
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            role=role,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self ,email ,username, phone, role, password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            role=role,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Holder(AbstractBaseUser):
    email=  models.EmailField(verbose_name="email", max_length=50, unique=True)
    username=   models.CharField(max_length=30, unique=True)
    phone=  models.BigIntegerField(unique=True)
    role=   models.IntegerField()
    date_joined=    models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
    last_login= models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin=   models.BooleanField(default=False)
    is_active=  models.BooleanField(default=True)
    is_staff=   models.BooleanField(default=False)
    is_superuser=   models.BooleanField(default=False)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email','password','phone','role']
    
    objects=MyHolderManager()
    
    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_lable):
        return True
        
class item(models.Model):
    item_name = models.CharField(max_length=20)
    item_price = models.IntegerField()
    
class orders(models.Model):
    username = models.CharField(max_length=50)
    ph_num = models.BigIntegerField()
    total_quantity = models.IntegerField()
    total_price = models.IntegerField()
    date =  models.DateTimeField(default=datetime.now(), blank=True)