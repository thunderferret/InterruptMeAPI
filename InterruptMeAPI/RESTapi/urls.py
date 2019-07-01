from django.urls import path

from . import views

urlpatterns = [
    path('user/<char:uuid>', views.user_settings, name = 'user_settings'),
]
