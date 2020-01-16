from django.db import models

# Create your models here.
class RegistrationData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    username=models.CharField(max_length=50)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    def __str__(self):
        return self.first_name