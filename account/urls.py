from django.urls import path
from . import views

urlpatterns = [
    path('logup/', views.UserFormView.as_view(), name='logup'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.LogInUser.as_view(), name='login')
]
