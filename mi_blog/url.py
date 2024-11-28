from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('publicacion/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]