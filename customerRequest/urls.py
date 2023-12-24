from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import Modal, MoveCardView, createOnBoardRequest,CRM, CompanyProfile, RegisterView, HomeView


urlpatterns = [
    path('request/',login_required(createOnBoardRequest.as_view()), name='create-request'),
    path('crm/', login_required(CRM.as_view()), name='crm'),
    path('', HomeView.as_view(), name='home'),
    path('profile/', login_required(CompanyProfile.as_view()), name='profile'),
    path('move_card/', MoveCardView.as_view(), name='move_card'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('modal/', login_required(Modal.as_view()), name='modal'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customerRequest/home.html'), name='logout'),
]
