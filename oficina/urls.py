from django.urls import path
from . import view_cbv 

urlpatterns = [
    path('', view_cbv.IndexView.as_view(), name='index'),
    path('motoristas/', view_cbv.MotoristaListView.as_view(), name='motorista_list'),
    path('motoristas/<int:pk>/', view_cbv.MotoristaDetailView.as_view(), name='motorista_detail'),
    path('motoristas/novo/', view_cbv.MotoristaCreateView.as_view(), name='motorista_create'),
    path('motoristas/<int:pk>/editar/', view_cbv.MotoristaUpdateView.as_view(), name='motorista_update'),
    path('motoristas/<int:pk>/deletar/', view_cbv.MotoristaDeleteView.as_view(), name='motorista_delete'),
]