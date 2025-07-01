from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return f'images/user_{instance.user.id}/profile_images_{filename}'

class Santri(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil_user')
    nama = models.CharField(max_length=255)
    nisn = models.IntegerField(default=0, unique=True)
    kota_lahir = models.CharField(max_length=30)
    tanggal_lahir = models.DateField(blank=True, null=True)
    GENDER_CHOICES = ((True, 'Laki-laki'),(False, 'Perempuan'),)
    gender = models.BooleanField(choices=GENDER_CHOICES, blank=True, null=True)
    alamat = models.CharField(max_length=255)
    foto = models.ImageField(upload_to=user_directory_path, blank=True)
    kelas = models.IntegerField(blank=True, null=True)
    ayah = models.CharField(max_length=255)
    pekerjaan_ayah = models.CharField(max_length=20)
    nomor_ayah = models.CharField(max_length=20)
    ibu = models.CharField(max_length=255)
    pekerjaan_ibu = models.CharField(max_length=20)
    nomor_ibu = models.CharField(max_length=20)
    wali = models.CharField(max_length=255)
    pekerjaan_wali = models.CharField(max_length=20)
    nomor_wali = models.CharField(max_length=20)
