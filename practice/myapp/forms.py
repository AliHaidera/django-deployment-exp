from django import forms
from myapp.models import userprofileinfo
from django.contrib.auth.models import User


class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=("username","email","password")


class userinfoform(forms.ModelForm):
    class Meta():
        model=userprofileinfo
        fields=("userurl","picture")
