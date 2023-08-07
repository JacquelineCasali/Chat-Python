from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
    # rotas
path('',views.frontpage,name='frontpage'),
path('cadastro/', views.cadastro,name='cadastro'),
path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]