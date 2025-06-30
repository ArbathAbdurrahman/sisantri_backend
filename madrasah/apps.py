from django.apps import AppConfig


class MadrasahConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'madrasah'
    
    def ready(self):
        import madrasah.signals