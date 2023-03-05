from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.api.serializers import MyTokenObtainPairSerializer, PasswordChangeSerializer, RegistrationSerializer, UpdateProfileSerializer, UpdateSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import UpdateAPIView
from accounts.models import User, UserProfile


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):

    routes = [
        '/api/token/',
        '/api/token/refresh/',
    ]
    return Response(routes)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = user.email
            data['username'] = user.username
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['phone'] = user.phone
            data['role'] = user.role
            data['password'] = user.password
            token = get_tokens_for_user(user)
            data['refresh'] = token['refresh']
            data['access'] = token['access']

            profile_serializer = UserProfileSerializer(data=data)
            if profile_serializer.is_valid():
                profile_serializer.create(user=user)   

        else:
            data = serializer.errors
        return Response(data)
    


class UpdateUserView(UpdateAPIView):
    serializer_class = UpdateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance


class UpdateProfileView(UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


    def get_object(self):
        profile = UserProfile.objects.get(user=self.request.user)
        return profile

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.update(serializer.instance, serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, instance, validated_data):
        instance.profile_pictures = validated_data.get('profile_pictures', instance.profile_pictures)
        instance.save()
        return instance     
