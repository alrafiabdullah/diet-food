from rest_framework import serializers
from django.contrib.auth import login, logout, authenticate

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "confirm_password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        if validated_data["password"] != validated_data["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "passwords don't match!"})

        user = User.objects.create_user(
            validated_data["username"], validated_data["email"], validated_data["password"],)

        user.is_customer = True
        user.save()

        return user


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "confirm_password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        if validated_data["password"] != validated_data["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "passwords don't match!"})

        user = User.objects.create_user(
            validated_data["username"], validated_data["email"], validated_data["password"],)

        user.is_employee = True
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password",)
        extra_kwargs = {"password": {"write_only": True}}
