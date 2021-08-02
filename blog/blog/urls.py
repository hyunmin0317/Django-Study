from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
]