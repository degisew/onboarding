import json
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .form import LoginForm, RegisterForm, CustomerRequestForm, CompanyProfileForm
from .models import CustomerRequest, Company
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# @login_required(login_url='/login/')


class HomeView(View):
    def get(self, request):
        return render(request, 'customerRequest/home.html')

class createOnBoardRequest(View):
    form_class = CustomerRequestForm
    template_name = 'customerRequest/form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class()
        user = request.user
        description = request.POST.get('description')
        service_type = request.POST.get('service_type')
        number_of_users = request.POST.get('users')
        about = request.POST.get('about_platform')
        expected_date = request.POST.get('expected_date')
        comments = request.POST.get('comments')
        new_request = CustomerRequest(user=user, service_type=service_type, number_of_users=number_of_users,
                                      about_platform=about, request_description=description, expected_date=expected_date, anything_else=comments)
        if new_request:
            new_request.save()
        return render(request, self.template_name)


class CompanyProfile(View):
    form_class = CompanyProfileForm
    template_name = 'customerRequest/profile.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print("###########", {**request.POST})
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('create-request')
        return render(request, self.template_name)


class CRM(View):
    def get(self, request, *args, **kwargs):
        # requests = CustomerRequest.objects.filter(status='initiation')
        # rs = User.objects.all()
        # for r in rs:
        #     print("*********************",r.company )
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
    template_name = 'customerRequest/register_form.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='home')

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


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(View):
    form_class = LoginForm
    template_name = 'customerRequest/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            s = auth.login(request, user)
            print(user, s)
            print(user.username)

            try:
                Company.objects.get(user=user)
                return redirect('create-request')

            except Company.DoesNotExist:
                return redirect('profile')

        else:
            return HttpResponse('Authentication Failed!')

    # def form_valid(self, form):
    #     remember_me = form.cleaned_data.get('remember_me')

    #     if not remember_me:
    #         # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
    #         self.request.session.set_expiry(0)

    #         # Set session as modified to force data updates/cookie to be saved.
    #         self.request.session.modified = True

    #     # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
    #     return super(CustomLoginView, self).form_valid(form)
