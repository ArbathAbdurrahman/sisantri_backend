from django.urls import path
from .views import AkademikView

app_name = "akademik"

urlpatterns = [
    path('/',AkademikView.as_view(), name='akademik')
]