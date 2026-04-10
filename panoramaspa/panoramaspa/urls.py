from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('recuperar/', views.recuperar_contrasena, name='recuperar'),
    path('perfil/', views.perfil, name='perfil'),

    path('admin-panel/', views.admin_panel, name='admin_panel'),

    path('feria-emprendedores/', views.feria_emprendedores, name='feria_emprendedores'),
    path('feria-comida/', views.feria_comida, name='feria_comida'),
    path('concierto/', views.concierto, name='concierto'),
    path('trekking/', views.trekking, name='trekking'),

    path('logout/', views.logout_view, name='logout'),
]