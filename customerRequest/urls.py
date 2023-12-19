from django.urls import path
from .views import MoveCardView, createOnBoardRequest,CRM, register, user_login, user_logout


urlpatterns = [
    path('request/', createOnBoardRequest.as_view(), name='create-request'),
    path('crm/', CRM.as_view(), name='crm'),
     path('move_card/', MoveCardView.as_view(), name='move_card'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
