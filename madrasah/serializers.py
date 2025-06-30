from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import *

class MadrasahSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfilMadrasah
        fields = '__all__'

class MisiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Misi
        fields = ['id','profil', 'isi']
        extra_kwargs = {'isi': {'required': True},'profil': {'required': False},}

    def create(self, validated_data):
        request = self.context.get('request')
        profil_id = self.context.get('id')
        instance = instance = get_object_or_404(ProfilMadrasah, id=profil_id)
        validated_data['profil'] = instance
        return super().create(validated_data)


    

class ProgramUnggulanSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProgramUnggulan
        fields = '__all__'

class ProgramSerializers(serializers.ModelSerializer):
    class Meta:
        model = IsiProgram
        fields= '__all__'