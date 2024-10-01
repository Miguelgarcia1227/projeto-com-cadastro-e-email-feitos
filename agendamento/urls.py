from django.urls import path
from . import views

urlpatterns = [
    path('', views.agendamento, name='agendamento'),
    path('novo/', views.novo_agendamento, name='novo_agendamento'),
    path('editar/<int:pk>/', views.agendamento_update, name='agendamento_update'),
    path('excluir/<int:pk>/', views.agendamento_delete, name='agendamento_delete'),
]



