from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class CustomJWTSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token["is_superuser"] = user.is_superuser

#         return token


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=127)
    email = serializers.EmailField(max_length=127)
    birthdate = serializers.DateField(allow_null=True, default=None)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=127, write_only=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self, obj: User) -> int:
        return obj.movies.count()

    def create(self, validated_data: dict) -> User:
        if self["is_employee"] is True:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create(**validated_data)

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=127, write_only=True)
    password = serializers.CharField(max_length=127, write_only=True)
