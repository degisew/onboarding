import json
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import auth
from .form import CustomerRequestForm, CreateUserForm, LoginForm
from .models import CustomerRequest

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# @login_required(login_url='/login/')
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
    def get(self, request, *args, **kwargs):
        # requests = CustomerRequest.objects.filter(status='initiation')
        stages = [
            {'id': 1, 'name': 'Initiation', 'cards': CustomerRequest.objects.filter(status='initiation')},
            {'id': 2, 'name': 'Processing', 'cards': CustomerRequest.objects.filter(status='Processing')},
            {'id': 3, 'name': 'Completed', 'cards': CustomerRequest.objects.filter(status='Completed')},
        ]
        return render(request, 'customerRequest/crm.html', {'stages': stages})

@method_decorator(csrf_exempt, name='dispatch')
class MoveCardView(View):
    def post(self, request, *args, **kwargs):
        data=json.loads(request.body)
        cardId = data.get('cardId')
        to_id = data.get('toId')
        print(cardId,to_id)
        print(request.body)
        # Logic to move card in the backend (update CRM status)
        # For simplicity, we'll just update the status field in the model
        card = CustomerRequest.objects.get(id=cardId)
        card.status = to_id
        card.save()

        return JsonResponse({'success': True})








def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateUserForm()
            return redirect('login')
    else:
        form = CreateUserForm()

    return render(request, 'customerRequest/login_register_form.html', {'form': form, 'btn_value': 'Register'})


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('create-transact')
        else:
            return HttpResponse('Authentication Failed!')
        
    return render(request, 'customerRequest/login_register_form.html', {'form':form, 'btn_value': 'login'})


def user_logout(request):
    auth.logout(request)
    return redirect('login')