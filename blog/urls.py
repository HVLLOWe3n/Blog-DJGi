from django.urls import path                    # import function path
from . import views                             # import file views from blog directory

urlpatterns = [
    path('', views.post_list),
    path('post/(P<pk>\d+)/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/(P<pk>\d+)/edit/', views.post_edit, name='post_edit'),
]
