from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import *

""" Signal untuk membuat data dengan id=1 """
@receiver(post_migrate)
def create_default_profil_madrasah(sender, **kwargs):
    if sender.name != 'madrasah':
        return

    ProfilMadrasah.objects.get_or_create(
        id=1,
        defaults={
            'nama': 'Madrasah Default',
            'alamat': 'Alamat Default',
            # tambah field lain yang wajib diisi
        }
    )