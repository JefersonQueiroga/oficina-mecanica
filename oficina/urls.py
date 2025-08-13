from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('motoristas/', views.motorista_list_view, name='motorista_list'),
    path('motoristas/<int:pk>/', views.motorista_detail_view, name='motorista_detail'),
    path('motoristas/novo/', views.motorista_create_view, name='motorista_create'),
    path('motoristas/<int:pk>/editar/', views.motorista_update_view, name='motorista_update'),
    path('motoristas/<int:pk>/deletar/', views.motorista_delete_view, name='motorista_delete'),
]