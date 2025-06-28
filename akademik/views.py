from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class AkademikView(APIView):
    def get():
        return print('get')