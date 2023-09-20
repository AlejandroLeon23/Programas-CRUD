"""
URL configuration for mi_tarea project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mi_app import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tarea/<int:pk>/', views.detalle_tarea, name='detalle_tarea'),
    path('tarea/crear/', views.crear_tarea, name='crear_tarea'),
    path('tarea/editar/<int:pk>/', views.editar_tarea, name='editar_tarea'),
    path('tarea/eliminar/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),
]

