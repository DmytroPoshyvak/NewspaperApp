from django import forms
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from . import models

class MyPersonalUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
    class Meta:
        model = models.PersonalCustomUser
        fields =  ('username', 'email', 'age',)

class MyPersonalUserChangeForm(UserChangeForm):
    class Meta:
        model = models.PersonalCustomUser
        fields =  ('username', 'email', 'age',)