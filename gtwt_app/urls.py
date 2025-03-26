from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),        # ✅ THIS MUST MATCH THE NAME IN YOUR TEMPLATE
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]