from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated
from rest_framework import status
from .serializers import *
from .models import ProfilMadrasah

from rest_framework.permissions import AllowAny, IsAdminUser

class MadrasahView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]

    def get(self, request, id):
        profil_madrasah = get_object_or_404(ProfilMadrasah, id=id)
        serializer = MadrasahSerializers(profil_madrasah)
        return Response(serializer.data)

    def patch(self, request, id):
        profil_madrasah = get_object_or_404(ProfilMadrasah, id=id)
        serializer = MadrasahSerializers(profil_madrasah, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MisiView(APIView):
    parser_classes = [FormParser, JSONParser]
    def get_permissions(self):
        if self.request.method in ['POST','PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]

    def get(self, request, id):
        profil = get_object_or_404(ProfilMadrasah, id=id)
        misi_madrasah = Misi.objects.filter(profil=profil)
        serializer = MisiSerializers(misi_madrasah, many=True)
        return Response(serializer.data)
    
    def post(self, request, id):
        serializer = MisiSerializers(data=request.data, context={'request': request, 'id':id})
        if serializer.is_valid():
            misi_madrasah = serializer.save()
            return Response({
                "detail": "Misi berhasil ditambahkan!",
                "data": MisiSerializers(misi_madrasah).data
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteMisiView(APIView):
    parser_classes = [FormParser, JSONParser]
    def get_permissions(self):
        if self.request.method in ['POST','PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]
    
    def patch(self, request, id):
        misi = get_object_or_404(Misi, id=id)
        serializer = MisiSerializers(misi, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            updated_misi = serializer.save()
            return Response({
                "detail": "Misi berhasil diperbarui.",
                "data": MisiSerializers(updated_misi).data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        misi = get_object_or_404(Misi, id=id)
        misi.delete()
        return Response({"detail": "Misi berhasil dihapus."}, status=status.HTTP_204_NO_CONTENT)
    