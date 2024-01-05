from django import forms
from .models import Registation_details,Upload_File


class RegistationForm(forms.ModelForm):
    class Meta:
        model=Registation_details
        fields=['Name','email','password']
        widgets = {
        'password': forms.PasswordInput(),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=Registation_details
        fields=['email','password']
        widgets = {
        'password': forms.PasswordInput(),
        }

class UploadForm(forms.ModelForm):
    class Meta:
        model=Upload_File
        fields=['upload']