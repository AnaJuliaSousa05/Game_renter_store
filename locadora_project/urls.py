from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views #importando a view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_jogos, name='home'),
    path ('cadastro/', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path ('alugar/<int:jogo_id>/', views.alugar_jogo, name='alugar_jogo'),
    path('meus-jogos/', views.meus_jogos, name='meus_jogos'),
    path('devolver/<int:locacao_id>/', views.devolver_jogo, name='devolver_jogo'), 
]
