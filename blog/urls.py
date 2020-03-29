from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create/', views.create, name='blog_create'),
    path('<int:pk>/update/', views.update, name='post_update'),
    path('<slug:slug>/', views.post, name='post'),
]
