from django.contrib import admin

from .models import Person
from .models import Profile
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    fields=['date','text']

admin.site.register(Person)

class ProfileAdmin(admin.ModelAdmin):
    fields=['name','productID','description','img']
admin.site.register(Profile)

