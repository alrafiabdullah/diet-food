from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

urlpatterns = [
    path("user", views.CustomerList.as_view()),
    path("customer/registration", views.CustomerRegistration.as_view()),
    path("employee/registration", views.EmployeeRegistration.as_view()),
    path("login", views.UserLogin.as_view()),

    path('token', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
