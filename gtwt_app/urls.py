from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # Password reset flow
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='auth/password_reset.html'
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Construction Mapping
    path("map/", views.map_view, name="map_view"),
    path("submit-zone/", views.submit_zone, name="submit_zone"),

    # Admin Zone Review
    path("admin/zones/", views.admin_zones, name="admin_zones"),
    path("admin/zones/verify/<int:zone_id>/", views.verify_zone, name="verify_zone"),
    path("admin/zones/delete/<int:zone_id>/", views.delete_zone, name="delete_zone"),

    # Saving and fetching zones
    path('api/save_zone/', views.save_zone, name='save_zone'),
    path('api/get_zones/', views.get_zones, name='get_zones'),

    path('my-reports/', views.my_reports, name='my_reports'),
    path("delete-zone/", views.delete_zone, name="delete_zone"),

    # Routes
    path('api/save_route/', views.save_route, name='save_route'),
    path('my-routes/', views.my_routes, name='my_routes'),
    path("api/rename_route/", views.rename_route, name="rename_route"),
]