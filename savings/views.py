from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, viewsets, generics
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# from .forms import AimsForm
# from datetime import datetime
from .serializers import AimSerializer, UserSerializer, RegisterSerializer
# import math
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from knox.models import AuthToken


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


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":
            UserSerializer(user, context=self.get_serializer_context()).data,
            "token":
            AuthToken.objects.create(user)[1]
        })


# class Registration_view(APIView):
#     ''' Creates the user '''
#     def post(self, request, format='json'):
#         if request.method == 'POST':
#             serializer = RegisterSerializer(data=request.data)
#             data = {}
#             if serializer.is_valid():
#                 user = serializer.save()
#                 data['response'] = 'Succesfully registered a new user.'
#                 data['email'] = user.email
#                 data['username'] = user.username
#             else:
#                 data = serializer.errors
#             return Response(data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# def calculate_finances(request):
#     ''' Takes all Aim objects from db and generate dynamic template using this objects '''
#     aims = Aim.objects.all()
#     # Here I calculate the sum cost of all aims and Here I create functionality that calculate monthly savings
#     sum = 0
#     weekly_sum = 0
#     now = datetime.now().date()
#    ''' pip install datetime and import'''
#     for aim in aims:
#         sum += aim.price
#         delta = now - aim.data
#         weekly_sum += aim.price / delta.days * 7

#     weekly_sum = math.ceil(abs(weekly_sum))

#     return render(request, 'cele.html', {
#         'cele': aims,
#         'suma': sum,
#         'weekly_sum': weekly_sum
#     })
