from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from .serializers import UserSerializer, CustomerRegistrationSerializer, EmployeeRegistrationSerializer, LoginSerializer
from .models import User


# Create your views here.
class CustomerList(ListAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        users = User.objects.all().order_by("id")
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerRegistration(GenericAPIView):
    serializer_class = CustomerRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class EmployeeRegistration(GenericAPIView):
    serializer_class = EmployeeRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class UserLogin(GenericAPIView):
    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        user = authenticate(
            request, username=request.data["username"], password=request.data["password"])
        if user is not None:
            login(request, user)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
