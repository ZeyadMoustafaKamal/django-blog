from django.urls import path
from . import views
urlpatterns =[
    path('create', views.create_post, name='create_post'),
    path('posts', views.Posts.as_view(), name='posts'),
]