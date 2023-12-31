from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Company, CustomerRequest


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
        fields = ['company_name', 'country', 'city', 'phone',
                  'tin_number', 'business_classification', 'industry']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Company name',
                'class': 'form-control'  # Here we have set a bootstrap class
            }),
            'country': forms.Select(
                choices=COUNTRY_CHOICES,
                attrs={
                    'type': 'select',
                    'class': 'form-control' 
                }),
            'city': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'city',
                'class': 'form-control' 
            }),
            'phone': forms.NumberInput(attrs={
                'type': 'text',
                'placeholder': 'company phone number',
                'class': 'form-control'
            }),
            'tin_number': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'enter tin number',
                'class': 'form-control'
            }),
            'business_classification': forms.TextInput(
                attrs={
                    'type': 'text',
                    'placeholder': 'business type',
                    'class': 'form-control'
                }),
            'industry': forms.Select(
                choices=INDUSTRY_CHOICES,
                attrs={
                    'type': 'select',
                    'placeholder': 'Industry type',
                    'class': 'form-control'
                }),
        }


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


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
