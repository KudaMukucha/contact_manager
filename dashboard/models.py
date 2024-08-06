from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=False)
    phone_number = PhoneNumberField(unique = True,blank=False)
    is_deleted = models.BooleanField(default=False)
    email = models.EmailField(max_length=300,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.phone_number} {self.email}'