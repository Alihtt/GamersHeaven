from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email(data):
    if "admin" in data.lower():
        raise serializers.ValidationError("email cant be `admin`")
    else:
        return data


class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password_confirm")
        extra_kwargs = {
            "email": {"validators": (clean_email,)},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        del validated_data["password_confirm"]
        return User.objects.create_user(**validated_data)

    def validate_username(self, data):
        if data.lower() == "admin":
            raise serializers.ValidationError("Username cant be `admin`")
        else:
            return data

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("Passwords must match")
        else:
            return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
