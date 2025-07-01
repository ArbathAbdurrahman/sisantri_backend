from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'akun'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('santri/', SantriListCreateAPIView.as_view(), name='santri-list-create'),
    path('santri/<int:pk>/', SantriDetailAPIView.as_view(), name='santri-detail'),
]