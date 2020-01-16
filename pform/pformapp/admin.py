from django.contrib import admin

# Register your models here.
from . models import ContactData

class ContactDataAdmin(admin.ModelAdmin):
    admin.site.register(ContactData)