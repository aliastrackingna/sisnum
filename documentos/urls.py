from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('incrementar/<int:tipo_id>/', views.incrementar, name='incrementar'),
    path('zerar/', views.zerar_todos, name='zerar_todos'),
    path('excluir/<int:tipo_id>/', views.excluir_tipo, name='excluir_tipo'),
    path('editar/<int:tipo_id>/', views.editar_numero, name='editar_numero'),
]
