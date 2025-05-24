from django.urls import path
from .views import (
    home_view,
    product_list_view,
    product_create_view,
    product_update_view,
    product_delete_view,
)

urlpatterns = [
    path('', home_view.as_view(), name='home'),
    path('list/', product_list_view.as_view(), name='product_list'),
    path('products/create/', product_create_view.as_view(), name='product_create'),
    path('update/<int:product_id>/', product_update_view.as_view(), name='product_update'),
    path('delete/<int:product_id>/', product_delete_view.as_view(), name='product_delete'),
]
