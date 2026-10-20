from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class StudentForm(forms.ModelForm):
     class Meta:
        model = student
        fields =('__all__')

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input Username',
        }),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input Email',
        }),
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input Password',
        }),
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
        }),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']  
class LoginForm(AuthenticationForm): 
    username = forms.CharField(
            label='Username',
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input Username',
            }),
        )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input Password',
        }),
    ) 
    class  Meta:
        model = CustomUser
        fields = ['username','password']
            