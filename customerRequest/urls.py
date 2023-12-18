from django.urls import path
from .views import createOnBoardRequest,CRM


urlpatterns = [
    path('request/', createOnBoardRequest.as_view(), name='create-request'),
    path('crm/', CRM.as_view(), name='crm')
]
