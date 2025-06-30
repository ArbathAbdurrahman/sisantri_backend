from django.urls import path
from .views import *

app_name = "madrasah"

urlpatterns = [
    path('/<int:id>', MadrasahView.as_view(), name='madrasah'),
    path('/<int:id>/misi', MisiView.as_view(), name='misi'),
    path('/misi/<int:id>', DeleteMisiView.as_view(), name='delete-misi')
]