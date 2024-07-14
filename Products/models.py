from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


# CLASE ESTADO

class Estado(models.Model):
    simbolo = models.CharField(max_length=1, primary_key=True)
    nombre = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.simbolo
    
    
# CLASE USUARIO BASE
class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        STAFF = "STAFF", "Staff"
        CUSTOMER = "CUSTOMER", "Customer"
        
    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, default="A", null=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:        
            self.role = self.base_role 
            return super().save(*args, **kwargs)
    


# CLASE STA
class StaffManager(BaseUserManager):
    def get_queryset(self, *arg, **kwargs):
        results = super().get_queryset(*arg, **kwargs)
        return results.filter(role=CustomUser.Role.STAFF)
    

class Staff(CustomUser):
    base_role = CustomUser.Role.STAFF
    staff = StaffManager()
    
    class Meta:
        proxy = True

@receiver(post_save, sender=Staff)
def create_staff_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STAFF":
        StaffProfile.objects.create(user=instance)


class StaffProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    staff_id = models.IntegerField(null=True, blank=True)
    
    


# CLASE CUSTOMER
    
class CustomerManager(BaseUserManager):
    def get_queryset(self, *arg, **kwargs):
        results = super().get_queryset(*arg, **kwargs)
        return results.filter(role=CustomUser.Role.CUSTOMER)
    

class Customer(CustomUser):
    base_role = CustomUser.Role.STAFF
    staff = CustomerManager()
    
    class Meta:
        proxy = True
   
@receiver(post_save, sender=Customer)
def create_staff_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)


class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    staff_id = models.IntegerField(null=True, blank=True)
    

# CATEGORIA

        
class Category(models.Model):
    name = models.CharField(max_length=100)
    decription = models.TextField(null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, default="A", null=True)

    def __str__(self):
        return self.name


# PRODUCTOS
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=200)
    price = models.PositiveSmallIntegerField(default=0)
    category = models.BooleanField(default=True)
    stock = models.PositiveSmallIntegerField(default=0)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, default="A", null=True)    
    
    def __str__(self):
        return self.name


