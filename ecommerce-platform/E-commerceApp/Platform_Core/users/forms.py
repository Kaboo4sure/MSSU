from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role']  # exclude password; handled separately

class CustomPasswordChangeForm(PasswordChangeForm):
    pass
