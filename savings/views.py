from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, viewsets, generics
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .serializers import AimSerializer, UserSerializer, RegisterSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


@api_view(['GET'])
def api_overview(request):

    api_urls = {
        'List': '/aim-list',
        'User_aims_list': '/<username>/aim-list',
        'Create': '<username>/aim-create',
        'Update': '/aim-update/<str:pk>/',
        'Delete': '/aim-delete/<str:pk>/',
        'Login': '/login',
        'Logout': '/logout',
        'Logout_tall': '/logoutall',
        'Register': '/register',
    }

    return Response(api_urls)


@api_view(['GET'])
def aim_list(request):
    aims = Aim.objects.all()
    serializer = AimSerializer(aims, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_aim_list(request, username):
    user = User.objects.get(username=username)
    aims = Aim.objects.filter(owner=user.id)
    serializer = AimSerializer(aims, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def aim_create(request, username):
    '''
    {
        "aim": <"str">,
        "data": <"yyyy-mm-dd">,
        "price": <int>
    }
    '''

    user = User.objects.get(username=username)
    aim = Aim(owner=user)

    serializer = AimSerializer(aim, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def aim_update(request, pk):
    '''
    {
        "id": <int>,
        "aim": <str>,
        "data": <"yyyy-mm-dd">,
        "price": <int>,
        "owner": <str>
    }
    '''

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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny, )
    '''
    {
        "username": <str>,
        "password": <str>
    }
    '''
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
