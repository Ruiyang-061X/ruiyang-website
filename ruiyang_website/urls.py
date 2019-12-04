from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_index/', views.blog_index, name='blog_index'),
    path('blog/<int:blog_id>/', views.blog_content, name='blog_content'),
]