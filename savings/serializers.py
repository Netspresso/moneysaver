from rest_framework import serializers
from .models import Aim


class AimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aim
        fields = '__all__'