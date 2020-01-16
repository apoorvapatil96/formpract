from django.db import models

# Create your models here.
class ContactData(models.Model):
    name=models.CharField(max_length=30)
    salary=models.IntegerField()
    email=models.EmailField(max_length=100)
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.name