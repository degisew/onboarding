from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .form import CustomerRequestForm
from .models import CustomerRequest

# Create your views here.


class createOnBoardRequest(View):
    form_class = CustomerRequestForm
    template_name = 'customerRequest/form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            print(form.cleaned_data)
            return HttpResponseRedirect("/success/")

        return render(request, self.template_name, {"form": form})
