from django.urls import path                    # import function path
from . import views                             # import file views from blog directory

urlpatterns = [
    path('', views.post_list),
    path('post/(?P<pk>\d+)/', views.post_detail, name='post_detail')
]
