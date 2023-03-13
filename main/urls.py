from django.urls import path 
from .views import SalesApiView


urlpatterns = [
    path('', SalesApiView.as_view()),
]
