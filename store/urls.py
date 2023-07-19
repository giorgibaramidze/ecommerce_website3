from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_slug>/<slug:sub_category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path("<slug:category_slug>/", views.product_by_category, name="product_list")
]

