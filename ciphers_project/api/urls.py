from django.urls import path
from .views import greeting, encode

urlpatterns = [
    path("", greeting, name="greeting"),
    path("caesar/<str:plaintext>/<int:shift>", encode, name="encode")
]