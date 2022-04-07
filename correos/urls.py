
from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import indexs, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path("kiwi/", indexs, name="index"),
    path("contacto/", contact, name="contacto"),
]
