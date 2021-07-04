from django import forms
from django.contrib.auth.models import User
from simple.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta():
        model = Registration
        fields = ('age','gender')

class BaseUserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')
