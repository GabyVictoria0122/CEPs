from django.urls import path

from . import views

urlpatterns = [
    path('cep/<cep>', views.api_ceps, name="ceps"),
    path('ola/', views.ola_ceps, name="olaceps"),
]
