from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Sign

class Log(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_Password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Sign
        fields = '__all__'

# class SignupForm(UserCreationForm):

#     class Meta(UserCreationForm.Meta):
#         model = get_user_model()
#         fields = ('username', 'email', 'first_name', 'last_name')
    


