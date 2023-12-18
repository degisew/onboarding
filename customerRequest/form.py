from django import forms
from .models import CustomerRequest

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
