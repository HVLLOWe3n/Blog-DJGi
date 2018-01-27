from django.urls import path                    # import function path
from . import views                             # import file views from blog directory

urlpatterns = [
    path('', views.post_list)
]
