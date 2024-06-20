from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # Adjust queryset if necessary
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)  # Allow unrestricted access for registration

# myapp/views.py

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

# myapp/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is the home page!")
