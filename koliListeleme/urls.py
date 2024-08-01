from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'koliListeleme'),
    path('<int:koliListeleme_id>', views.detay, name = 'detay'),
]