from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings
from .models import CustomerRequest, CustomUser

class CustomerRequestForm(forms.ModelForm):

    expected_date = forms.DateField(label='Expected Date', widget=forms.DateInput(
        attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
    ))
    class Meta:
        model = CustomerRequest
        fields = ['service_type', 'number_of_users', 'about_platform',
                  'request_description', 'expected_date', 'anything_else']
        
        # labels = ["", ""]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'username', 'email', 'password1' ,'password2']



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']