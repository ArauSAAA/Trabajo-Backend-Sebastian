from django.urls import path
from . import views

urlpatterns = [
    path('taquilla/', views.taquilla, name="my_taquilla"),
    path('login/', views.login, name="my_login"),
    path('index/', views.index, name="my_info"),
]