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
    # form_class = CustomerRequestForm
    template_name = 'customerRequest/form.html'

    def get(self, request):
        # form = self.form_class()
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        print(type(request.POST))
        service_type = request.POST.get('service_type')
        number_of_users = request.POST.get('users')
        about = request.POST.get('about_platform')
        description = request.POST.get('description')
        expected_date = request.POST.get('date')
        comments = request.POST.get('comments')
        new_request = CustomerRequest(service_type=service_type, number_of_users=number_of_users,
                                      about_platform=about, request_description=description, expected_date=expected_date, anything_else=comments)
        # if new_request.is_valid():
        # <process form cleaned data>
        # new_request.save()
        # new_request = cr()

        return render(request, self.template_name)


class CRM(View):
    def get(self, request, *args, **kwargs):
        # requests = CustomerRequest.objects.filter(status='initiation')
        stages = [
            {'id': 1, 'name': 'Initiation', 'cards': CustomerRequest.objects.filter(
                status='Initiation').order_by('-created_at')},
            {'id': 2, 'name': 'Proposition',
                'cards': CustomerRequest.objects.filter(status='Proposition')},
            {'id': 3, 'name': 'Negotiation',
                'cards': CustomerRequest.objects.filter(status='Negotiation')},
            {'id': 4, 'name': 'Won',
                'cards': CustomerRequest.objects.filter(status='Won')},
            {'id': 5, 'name': 'Lost',
                'cards': CustomerRequest.objects.filter(status='Lost')},
        ]
        return render(request, 'customerRequest/crm.html', {'stages': stages})


@method_decorator(csrf_exempt, name='dispatch')
class MoveCardView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        cardId = data.get('cardId')
        to_id = data.get('toId')
        print(cardId, to_id)
        print(request.body)
        # Logic to move card in the backend (update CRM status)
        # For simplicity, we'll just update the status field in the model
        card = CustomerRequest.objects.get(id=cardId)
        card.status = to_id
        card.save()

        return HttpResponse('success')


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

    return render(request, 'customerRequest/login_register_form.html', {'form': form, 'btn_value': 'login'})


def user_logout(request):
    auth.logout(request)
    return redirect('login')
