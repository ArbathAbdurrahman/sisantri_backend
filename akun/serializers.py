from rest_framework import serializers
from django.db import transaction
from .models import Santri
from django.contrib.auth.models import User

class SantriSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    user_username = serializers.CharField(source='user.username', read_only=True)
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Santri
        fields = [
            'id', 'nama', 'nisn', 'kota_lahir', 'tanggal_lahir', 'gender', 'alamat', 'foto',
            'kelas', 'ayah', 'pekerjaan_ayah', 'nomor_ayah', 'ibu', 'pekerjaan_ibu', 'nomor_ibu',
            'wali', 'pekerjaan_wali', 'nomor_wali',
            # Field untuk GET dan POST
            'user_username', 'gender_display', 'username', 'password', 'email', 'user'
        ]
        extra_kwargs = {
            'user': {'required': False},
            'password': {'style': {'input_type': 'password'}},
        }

    def validate_username(self, value):
        """Validasi jika username sudah ada."""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username ini sudah digunakan.")
        return value

    def validate_nisn(self, value):
        """
        Memastikan NISN unik, kecuali untuk instance yang sedang diupdate.
        """
        if self.instance:
            if self.instance.nisn == value:
                return value
        
        if Santri.objects.filter(nisn=value).exists():
            raise serializers.ValidationError("Santri dengan NISN ini sudah ada.")
        return value

    def validate_nomor_ayah(self, value):
        """
        Contoh validasi untuk memastikan nomor telepon diawali dengan '08'.
        """
        if not value.startswith('08'):
            raise serializers.ValidationError("Nomor telepon Ayah harus diawali dengan '08'.")
        return value
        
    def validate_nomor_ibu(self, value):
        """
        Contoh validasi untuk memastikan nomor telepon diawali dengan '08'.
        """
        if not value.startswith('08'):
            raise serializers.ValidationError("Nomor telepon Ibu harus diawali dengan '08'.")
        return value

    @transaction.atomic # Menjamin semua proses berhasil atau tidak sama sekali
    def create(self, validated_data):
        """
        Override method create untuk membuat User dan Santri sekaligus.
        """
        user_data = {
            'username': validated_data.pop('username'),
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password')
        }
        user = User.objects.create_user(**user_data)
        santri = Santri.objects.create(user=user, **validated_data)
        
        return santri