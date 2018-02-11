from django.urls import path
from . import views
from account.views import RegisterUserView

urlpatterns = [
    path('register/' , RegisterUserView.as_view() , name = 'register'),
    
]
