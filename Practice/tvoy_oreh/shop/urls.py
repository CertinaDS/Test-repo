from django.urls import path
from .views import product_list, product_detail  # Импорт конкретных функций
from . import views

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='index'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
]