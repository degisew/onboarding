from django.urls import path
from .views import createOnBoardRequest


urlpatterns = [
    path('request/', createOnBoardRequest.as_view(), name='create-request')
]
