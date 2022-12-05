"""fortraveler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'post'

urlpatterns = [
    path('', views.show_main_page, name='main'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('upload/', views.upload, name='upload'),
    path('post/', views.search_result, name='search_result'),
    path('post/<int:pk>/', views.show_post_detail, name='post_detail'),
    path('profile/<int:pk>/', views.show_post_detail, name='profile_detail'),
    path('profile/', views.profile_page, name='profile'),
    path('post/<int:pk>/<int:comment_pk>/delete',views.comment_delete,name='comment_delete'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('post/<int:pk>/update', views.post_update, name='update'),
]
