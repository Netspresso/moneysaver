from rest_framework import serializers
from .models import Aim
from django.contrib.auth.models import User


class AimSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Aim
        fields = ('id', 'aim', 'data', 'price', 'is_finished', 'owner')


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    aims = serializers.PrimaryKeyRelatedField(many=True,
                                              queryset=Aim.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'aims')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):

    # password2 = serializers.CharField(style={'input_type': 'password'},
    #                                   write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'])
        # user.set_password(validated_data['password'])
        return user