from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings
from .models import Company, CustomerRequest, CustomUser

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
        fields = ['expected_date']
        
        # labels = ["", ""]
class CompanyProfileForm(forms.ModelForm):
    class Meta:
        COUNTRY_CHOICES = [
            ('ETH', 'Ethiopia')
        ] 
        INDUSTRY_CHOICES = [
            ('IT', 'Information Technology'),
            ('finance', 'Finance'),
            ('healthcare', 'Healthcare'),
            ('business', 'Business')
        ]
        model = Company
        fields = ['name', 'country', 'city', 'phone', 'tin_number', 'business_classification', 'industry']
        widgets = {
            'name': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Company name',
                'class': 'form-control' # Here we have set a bootstrap class 
                }),
            'country': forms.Select(
                choices=COUNTRY_CHOICES,
                attrs={
            'type': 'select',
            'class': 'form-control' # Here we have set a bootstrap class 
            }),
            'city': forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'city',
            'class': 'form-control' # Here we have set a bootstrap class 
            }),
            'phone': forms.NumberInput(attrs={
            'type': 'text',
            'placeholder': 'city',
            'class': 'form-control' # Here we have set a bootstrap class 
            }),
            'tin_number': forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'city',
            'class': 'form-control' # Here we have set a bootstrap class 
            }),
            'business_classification': forms.TextInput(
                attrs={
            'type': 'text',
            'placeholder': 'country',
            'class': 'form-control' # Here we have set a bootstrap class 
            }),
            'industry': forms.Select(
                choices=INDUSTRY_CHOICES,
                attrs={
            'type': 'select',
            'class': 'form-control' # Here we have set a bootstrap class 
            }),
        }

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