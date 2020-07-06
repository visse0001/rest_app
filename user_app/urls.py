from django.urls import path
from user_app.views import UserRegistrationView, UserLoginView, UserProfileView

urlpatterns = [
    path('signup', UserRegistrationView.as_view()),
    path('signin', UserLoginView.as_view()),
    path('profile', UserProfileView.as_view()),
]
