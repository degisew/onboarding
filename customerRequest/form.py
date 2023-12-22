from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Company, CustomerRequest, Schedule


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
                    'class': 'form-control'  # Here we have set a bootstrap class
                }),
            'city': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'city',
                'class': 'form-control'  # Here we have set a bootstrap class
            }),
            'phone': forms.NumberInput(attrs={
                'type': 'text',
                'placeholder': 'company phone number',
                'class': 'form-control'  # Here we have set a bootstrap class
            }),
            'tin_number': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'enter tin number',
                'class': 'form-control'  # Here we have set a bootstrap class
            }),
            'business_classification': forms.TextInput(
                attrs={
                    'type': 'text',
                    'placeholder': 'business type',
                    'class': 'form-control'  # Here we have set a bootstrap class
                }),
            'industry': forms.Select(
                choices=INDUSTRY_CHOICES,
                attrs={
                    'type': 'select',
                    'placeholder': 'Industry type',
                    'class': 'form-control'  # Here we have set a bootstrap class
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


# class ModalForm(forms.ModelForm):
    # class Meta:
    #     ACTIVITY_CHOICES = [
    #         ('meeting', 'Meeting'),
    #         ('call', 'Call'),
    #         ('email', 'Email'),
    #     ]
    #     model = Schedule
    #     fields = ['activity_type', 'due_date', 'fee', 'summary']
        # widgets = {
        #     'activity_type': forms.Select(
        #         choices=ACTIVITY_CHOICES,
        #         attrs={
        #             'type': 'text',
        #             'placeholder': 'Company name',
        #             'class': 'form-control'  # Here we have set a bootstrap class
        #         }),
        #     'due_date': forms.DateTimeInput(
        #         attrs={
        #             'type': 'date',
        #             'placeholder': 'yyyy-mm-dd',
        #             'class': 'form-control'
        #         }
        #     ),
        #     'fee': forms.TextInput(attrs={
        #         'type': 'text',
        #         'placeholder': 'fee',
        #         'class': 'form-control'  # Here we have set a bootstrap class
        #     }),
        #     'summary': forms.Textarea(attrs={
        #         'type': 'textarea',
        #         'placeholder': 'type here...',
        #         'rows': 3, 
        #         # 'cols': 4,
        #         'class': 'form-control'  # Here we have set a bootstrap class
        #     }),

        # }
