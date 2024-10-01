# Importações necessárias para definir as rotas de URLs
from django.urls import path  # Importa a função path para definir as rotas de URL
from .views import home  # Importa a função de view 'home' do módulo 'views' local
from django.contrib.auth import views as auth_views  # Importa as views de autenticação do Django
from . import views
from .views import confirmaremail
from .views import CustomPasswordResetConfirmView


# Lista de padrões de URL para a aplicação 'core'
urlpatterns = [

    path('', home, name='home'),
    
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    
    path('planos/', views.planos, name='planos'),

    path('loginmedico/', views.loginmedico, name='loginmedico'),

    path('cadastro/', views.cadastro, name='cadastro'),
    
    path('esquecisenha/', auth_views.PasswordChangeView.as_view(template_name='core/esquecisenha.html'), name='esquecisenha'),
   
    path('dentista/', views.dentista, name='dentista'),
    
    path('cirurgia/', views.cirurgia, name='cirurgia'),
    
    path('implate/', views.implante, name='implante'),

    path('protese/', views.protese, name='protese'),
    
    path('invisalign/', views.invisalign, name='invisalign'),
    
    path('ortodontia/', views.ortodontia, name='ortodontia'),
    
    path('pediatra/', views.pediatra, name='pediatra'),
    
    path('geri/', views.geri, name='geri'),

    path('confirmaremail/', views.confirmaremail, name='confirmaremail'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password-reset/', views.password_reset_view, name='password_reset'),
]   