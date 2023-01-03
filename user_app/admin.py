from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from . import forms

class MyUserAdmin(UserAdmin):
    add_form = forms.MyPersonalUserCreationForm
    list_display = ['email' , 'username' , 'age' , 'is_staff' , 'is_active']
    model = models.PersonalCustomUser
    form = forms.MyPersonalUserChangeForm

admin.site.register(models.PersonalCustomUser , MyUserAdmin)