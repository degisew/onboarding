from django.urls import path
from .views import MoveCardView, createOnBoardRequest,CRM, CompanyProfile, RegisterView


urlpatterns = [
    path('request/', createOnBoardRequest.as_view(), name='create-request'),
    path('crm/', CRM.as_view(), name='crm'),
    path('profile/', CompanyProfile.as_view(), name='profile'),
    path('move_card/', MoveCardView.as_view(), name='move_card'),
    path('register/', RegisterView.as_view(), name='users-register'),
    # path('', home, name='users-home'),
    # path('register/', register, name='register'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
]
