from django.urls import path
from . import views

urlpatterns = [
    path('logup/', views.UserFormView.as_view(), name='logup')
]