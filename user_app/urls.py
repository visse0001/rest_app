from django.urls import path
from user_app.views import UserRegistrationView

urlpatterns = [
    path('signup', UserRegistrationView.as_view()),
]
