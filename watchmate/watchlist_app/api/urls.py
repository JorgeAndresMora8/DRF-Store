from django.urls import path
from watchlist_app.api.views import ProductListAV, ProductDetailAV, CategoryListAV, CategoryDetailAV
urlpatterns = [
    path('list/', ProductListAV.as_view(), name='product-list'), 
    path('<int:pk>/', ProductDetailAV.as_view(), name='product-detail'),
    path('category/', CategoryListAV.as_view(), name='category-list'), 
    path('category/<int:pk>', CategoryDetailAV.as_view(), name='category-detail')
]