from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .form import CustomerRequestForm
from .models import CustomerRequest


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
            form.save()
            form = self.form_class()

        return render(request, self.template_name, {"form": form})
    

class CRM(View):
    def get(self, request):
        requests = CustomerRequest.objects.all()
        return render(request, 'customerRequest/crm.html', {'requests': requests})
