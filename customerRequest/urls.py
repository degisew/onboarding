from django.urls import path
from django.contrib.auth import views as auth_views

from .form import LoginForm
from .views import CustomLoginView, MoveCardView, createOnBoardRequest,CRM, CompanyProfile, RegisterView, HomeView


urlpatterns = [
    path('request/', createOnBoardRequest.as_view(), name='create-request'),
    path('crm/', CRM.as_view(), name='crm'),
    path('', HomeView.as_view(), name='home'),
    path('profile/', CompanyProfile.as_view(), name='profile'),
    path('move_card/', MoveCardView.as_view(), name='move_card'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customerRequest/logout.html'), name='logout'),
]


# redirect_authenticated_user=True,template_name='customerRequest/login.html', authentication_form=LoginForm), 