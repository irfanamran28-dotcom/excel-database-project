from django.urls import path
from . import views


urlpatterns = [
    # Auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Excel Data
    path('data/', views.data_list_view, name='data_list_admin'),
    path('data/add/', views.data_add_view, name='data_add_admin'),
    path('data/edit/<int:pk>/', views.data_edit_view, name='data_edit_admin'),
    path('data/delete/<int:pk>/', views.data_delete_view, name='data_delete_admin'),
    path('data/export/', views.export_to_excel, name='export_excel'),  # Add this line
    
    # Friends
    path('friends/', views.friends_list_view, name='friends_list'),
    path('friends/add/', views.friend_add_view, name='friend_add'),
    path('friends/edit/<int:pk>/', views.friend_edit_view, name='friend_edit'),
    path('friends/delete/<int:pk>/', views.friend_delete_view, name='friend_delete'),
]


