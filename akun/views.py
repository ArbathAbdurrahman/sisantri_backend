from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import Http404

from .models import *
from .serializers import *
from .permissions import *

# class RegistrationView(APIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"detail": "{user.username} berhasil diregistrasi"})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'error': 'Username atau password salah!'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response({"error": "Invalid or expired refresh token"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class SantriListCreateAPIView(APIView):
    """
    GET: Boleh untuk semua pengguna yang login.
    POST: Hanya untuk admin.
    """
    def get_permissions(self):
        """Menentukan permission berdasarkan method request."""
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.IsAdminUser()]

    def get(self, request, format=None):
        santri_list = Santri.objects.all()
        serializer = SantriSerializer(santri_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SantriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SantriDetailAPIView(APIView):
    """
    GET: Boleh untuk pengguna yang login.
    PUT & DELETE: Hanya untuk admin.
    PATCH: Hanya untuk pemilik profil.
    """
    def get_permissions(self):
        """Menentukan permission berdasarkan method request."""
        if self.request.method == 'PATCH':
            return [IsOwnerOfProfile()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_object(self, pk):
        try:
            return Santri.objects.get(pk=pk)
        except Santri.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        santri = self.get_object(pk)
        serializer = SantriSerializer(santri)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        santri = self.get_object(pk)
        serializer = SantriSerializer(santri, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        santri = self.get_object(pk)
        serializer = SantriSerializer(santri, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        santri = self.get_object(pk)
        santri.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)