import json
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib import auth
from django.contrib import messages
from .form import LoginForm, RegisterForm, CustomerRequestForm, CompanyProfileForm
from .models import CustomerRequest, Company, Schedule
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .email import send_email


class HomeView(View):
    def get(self, request):
        return render(request, 'customerRequest/home.html')


class DashboardView(View):
    def get(self, request):
        if request.user.is_staff:
            return render(request, 'customerRequest/admin_dashboard.html')
        return render(request, 'customerRequest/user_dashboard.html')

class createOnBoardRequest(View):
    form_class = CustomerRequestForm
    template_name = 'customerRequest/form.html'

    def get(self, request):
        form = self.form_class()
        try:
            Company.objects.get(user=request.user)
            return render(request, self.template_name, {'form': form})

        except Company.DoesNotExist:
            return redirect('profile')

    def post(self, request, *args, **kwargs):
        form = self.form_class()
        user = request.user
        description = request.POST.get('description')
        offer = request.POST.get('offer')
        service_type = request.POST.get('service_type')
        number_of_users = request.POST.get('users')
        about = request.POST.get('about_platform')
        expected_date = request.POST.get('expected_date')
        comments = request.POST.get('comments')
        new_request = CustomerRequest(user=user, service_type=service_type, number_of_users=number_of_users, offer=offer,
                                      about_platform=about, request_description=description, expected_date=expected_date, anything_else=comments)
        if new_request:
            new_request.save()
            messages.success(request, 'Request Sent.')
            return redirect('dashboard')


class CompanyProfile(View):
    form_class = CompanyProfileForm
    template_name = 'customerRequest/profile.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('create-request')
        return render(request, self.template_name)


class CRM(View):
    def get(self, request, *args, **kwargs):
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


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'customerRequest/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='dashboard')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, 'customerRequest/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, 'customerRequest/register.html', {'form': form})


class CustomLoginView(View):
    form_class = LoginForm
    template_name = 'customerRequest/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class()
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials.')
            return render(request, self.template_name, {'form': form})

class Modal(View):
    # form_class = ModalForm
    template_name = 'customerRequest/modal.html'

    def post(self, request, *args, **kwargs):
        request_id = request.POST.get('request')
        try:
            request_instance = CustomerRequest.objects.get(id=request_id)
            activity_type = request.POST.get('activity_type')
            due_date = request.POST.get('due_date')
            summary = request.POST.get('summary')
            fee = request.POST.get('fee')
            new_schedule = Schedule(activity_type=activity_type, due_date=due_date,
                                    summary=summary, fee=fee, request=request_instance)
            if new_schedule:
                new_schedule.save()
                send_email(request_instance.user.email,
                           request_instance.user.first_name, due_date, activity_type)
                return redirect('crm')
        except CustomerRequest.DoesNotExist:
            print("Doesn't exist")
