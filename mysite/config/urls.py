from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    path('', views.index, name='index'),  # '/' 에 해당되는 path
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
]