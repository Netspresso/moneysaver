from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from .models import Aim
# from .forms import AimsForm
# from datetime import datetime
from .serializers import AimSerializer
# import math
from django.http import JsonResponse


@api_view(['GET'])
def api_overview(request):

    api_urls = {
        'List': '/aim-list',
        'Create': '/aim-create',
        'Update': 'aim-update/<str:pk>/',
        'Delete': 'aim-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def aim_list(request):
    aims = Aim.objects.all()
    serializer = AimSerializer(aims, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def aim_create(request):
    serializer = AimSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def aim_update(request, pk):
    aim = Aim.objects.get(id=pk)
    serializer = AimSerializer(instance=aim, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def aim_delete(request, pk):
    aim = Aim.objects.get(id=pk)
    aim.delete()

    return Response("Item succesfully deleted")