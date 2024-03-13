from django.urls import path
from . import views


urlpatterns = [
    path('', views.koloda_list, name='koloda_list'),
    
    path('koloda/<int:pk>/', views.koloda_detail, name='koloda_detail'),

    path('cart/<int:pk>/', views.cart_detail, name='cart_detail'),
    

    path('koloda/new/', views.koloda_new, name='koloda_new'),
    path('cart/new/', views.cart_new, name='cart_new'),
    
    path('koloda/<int:pk>/edit/', views.koloda_edit, name='koloda_edit'),
    path('cart/<int:pk>/edit/', views.cart_edit, name='cart_edit'),

    path('register/', views.register_view, name='register'),
    path('profil/', views.profil, name='profil'),
    
]
