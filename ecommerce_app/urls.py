from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('category_detail/', views.category_detail, name="category_detail"),
    path('product_list/', views.product_list, name="product_list"),
]
