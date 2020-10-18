from rest_framework import serializers
from .models import Aim
from django.contrib.auth.models import User


class AimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aim
        fields = '__all__'


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):

    # password2 = serializers.CharField(style={'input_type': 'password'},
    #                                   write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(validated_data['username'], validated_data['email'],
                    validated_data['password'])
        return user