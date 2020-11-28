from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='shop'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('box/', views.box, name='box'),
    path('box_length/', views.box_original, name='box_original'),
    path('box_lengths/', views.box_premium, name='box_premium'),
]